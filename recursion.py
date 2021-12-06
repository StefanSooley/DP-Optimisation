import numpy as np


# nodes = np.array([[2, 1], [[2, 3], [3, 2]]], dtype='object')

class Node:
    def __init__(self, up, dn, weight=0):
        self.weight = weight
        self.choice = None
        self.up = up
        self.dn = dn

    def __repr__(self):
        return (f"up : {self.up}, "
                f"down : {self.dn}, "
                f"weight : {self.weight}, "
                f"choice : {self.choice}")


class Graph:
    def __init__(self, node_list):
        self.node_list = node_list
        self.stages = []

    def def_nodes(self):
        """
        Converts the list of node data into a list of stages made of Node object instances
        """
        for idx, stage in enumerate(self.node_list):
            if idx == 0:
                self.stages.append([Node(stage[0], stage[1])])
            else:
                stage_list = []
                for node in stage:
                    stage_list.append(Node(node[0], node[1]))
                self.stages.append(stage_list)

        # Add a stage at the end representing the weights of 0 at the end
        self.stages.append([Node(0, 0, 0)] * len(self.node_list) * 2)

    def cheapest_path(self):
        n = len(self.stages)
        for idx, stage in enumerate(reversed(self.stages)):
            for jdx, node in enumerate(stage):
                if idx == 0:
                    pass
                else:

                    # The weights of the connecting nodes. The complicated indices find the nodes depending on the
                    # current indices

                    dn_w = self.stages[n - idx][2 * jdx + 1].weight
                    up_w = self.stages[n - idx][2 * jdx].weight

                    if node.dn + dn_w > node.up + up_w:
                        node.choice = "up"
                        node.weight += node.up + up_w
                    else:
                        node.choice = "down"
                        node.weight += node.dn + dn_w

    def find_path(self):

        init_choice = self.stages[0][0].choice
        rolling_i = 0 if init_choice == "up" else 1

        path = [init_choice]
        for stage in self.stages:
            print(stage)
        print(path)





# nodes = np.array([[2, 1], [2, 3, 3, 2]], dtype='object')
# choice_array = nodes.copy()
# strs = np.array([[0] * (x + 1) for x in range(len(nodes))], dtype='object')
#
#
# for idx, stage in reversed(list(enumerate(nodes))):
#     choices = iter(stage)
#     for jdx, choice in enumerate(choices):
#         print(choice_array)
#         if idx==0:
#             up_node_weight = 0
#             dn_node_weight = 0
#         else:
#             up_node_weight = choice_array[idx-1][0]
#             dn_node_weight = choice_array[idx-1][1]
#         up = choice + up_node_weight
#         dn = next(choices) + dn_node_weight
#         if up < dn:
#             strs[idx][jdx] = "up"
#             choice_array[idx][jdx] = up
#         else:
#             strs[idx][jdx] = "down"
#             choice_array[idx][jdx] = dn
#
# final_path_str = [0] * len(nodes)
# cost = [0] * len(nodes)
# print(choice_array)
# print(f"final path = {strs}")
#


# next_idx = 0
# for idx, stage in enumerate(strs):
#
#     print(next_idx)
#     final_path_str[idx] = strs[idx][next_idx]
#     cost[idx] = choice_array[idx][next_idx]
#
#     if stage[next_idx] == "down":
#         next_idx = 2 * next_idx + 1
#     else:
#         next_idx = 2 * next_idx
#
# print(final_path_str)
# print(sum(cost))
