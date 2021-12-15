import numpy as np


class Plan:
    def __init__(self, cost, return_):
        self.return_ = return_
        self.cost = cost

    def __repr__(self):
        return f"{self.cost, self.return_}"


class CGraph:
    def __init__(self, sub_list):
        self.sub_list = sub_list
        self.stages = []

    def sub_list2stages(self):
        """
        Turn the subsidiary cost and returns array into a list of Plan objects
        """
        for idx, sub in enumerate(self.sub_list):
            sub_plan = []
            for plan in sub:
                sub_plan.append(Plan(plan[0], plan[1]))
            self.stages.append(sub_plan)

    def optimal_values(self, x, stage_idx, single=True):
        """
        Makes the first optimal value calculation.
        :param x: The starting capital
        :param stage_idx: The index of the stage.
        :param single: True if just the highest value to be outputted, False if a list of values to output.
        :return: Returns a dictionary with the capital as the key and the highest returns as the values.
        """
        ov_list = []
        c = 2
        while c <= x:

            vals = []
            for idx, plan in enumerate(self.stages[stage_idx]):
                if c >= plan.cost:
                    vals.append(plan.return_)
            ov_list.append(vals)
            c += 1

        keys = [i for i in range(2, x + 1)]
        values = [None] * len(range(2, x + 1))

        dic = dict(zip(keys, values))
        ddic = {}

        for idx, returns in enumerate(ov_list):
            try:
                dic[idx + 2] = max(returns)
                ddic[idx + 2] = returns.index(max(returns)) + 1
            except:
                dic[idx + 2] = 0
                ddic[idx + 2] = returns.index(max(returns)) + 1
        if single:
            return max(list(dic.values()))
        else:

            return dic, ddic

    def max_return(self, capital):
        """
        Uses forward recursion to produce the table of returns and choices.
        :param capital: The initial starting capital
        :return: A tuple of lists of dictionaries, one with the plan choice at each stage and the other with the returns
        from the optimal solution.
        """
        # Find the optimal values the first time using the optimal value function
        dic, ddic = self.optimal_values(capital, 0, single=False)
        trace_l = [dic]
        d_trace_l = [ddic]

        # Feedforward part
        for idx, stage in enumerate(self.stages):
            if idx != 0:
                s_ = []
                sd_ = []
                for jdx, path in enumerate(stage):
                    s = trace_l[0].copy()
                    sd_ = d_trace_l[0].copy()
                    # Calculate objective value function
                    for i in range(2, capital + 1):
                        try:
                            s[i] = (path.return_ + trace_l[idx - 1][i - path.cost])
                            sd_[i] = jdx + 1
                        except:
                            s[i] = -1
                            sd_[i] = -1
                    s_.append(s)

                super_d = {i: -1 for i in range(2, capital + 1)}
                super_dd = super_d.copy()

                # Find the max from all the traces
                for idx_, ss in enumerate(s_):

                    for i in list(ss.keys()):

                        if ss[i] > super_d[i]:
                            super_d[i] = ss[i]
                            super_dd[i] = idx_ + 1

                d_trace_l.append(super_dd)
                trace_l.append(super_d)

        return d_trace_l, trace_l

    def calc_return_path(self, capital, d_dic_l, p_dic_l):
        """
        Goes through the dictionaries and finds the path to get the highest return.
        :param capital: The starting (total) capital
        :param d_dic_l: dictionary of optimal decisions at each capital
        :param p_dic_l: dictionary of optimal profits at each capital
        :return: A tuple containing the maximum profit, the chosen plans and total cost, and logs.
        """
        max_profit = p_dic_l[-1][capital]
        num = len(d_dic_l) - 1
        choices = []
        end_capital = capital
        for idx, d_dic in enumerate(reversed(d_dic_l)):
            plan_idx = d_dic[end_capital] - 1
            end_capital = end_capital - self.stages[num - idx][plan_idx].cost
            choices.append(plan_idx + 1)

        logs = [capital, d_dic_l, p_dic_l]

        choices = list(reversed(choices))
        total_cost = capital - end_capital
        return max_profit, choices, total_cost, logs

    def solve_capital_budgeting(self, capital):
        """
        Uses the class functions to solve the problem initiated
        :param capital: The initial capital
        :return: The maximum profit, the choices to get the maximum profit and the total cost in a tuple.
        """

        self.sub_list2stages()
        d, p = self.max_return(capital)
        max_profit, choices, total_cost, logs = self.calc_return_path(capital, d, p)
        return max_profit, choices, total_cost, logs
