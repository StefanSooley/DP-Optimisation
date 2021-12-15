from recursion import NGraph
from capital_budgeting import CGraph
from data import read_graph, save_logs
import numpy as np


def main():
    # Read the txt to get the node data
    nodes = read_graph('inputnetwork.txt')
    # Create the graph object using the node data
    graph1 = NGraph(nodes)
    # Find the solution
    solution1, networklogs = graph1.solve_cheapest_path()

    # Outputs
    print(f'{"=" * 12 + "Cheapest Path" + "=" * 12}\nCheapest path is: {solution1}\n')
    save_logs('lognetwork.txt', networklogs, solution1)

    # Read the txt to get the cost and return data
    sub_plans, capital = read_graph('inputcapbud.txt')
    # Generate the graph object with the plan data
    graph2 = CGraph(sub_plans)
    # Find the solution
    solution2 = graph2.solve_capital_budgeting(capital)

    # Outputs
    max_profit, choices, total_cost, capbudlogs = solution2
    print(f'{"=" * 12 + "Capital Budgeting" + "=" * 12}\n'
          f'max return: {max_profit}, choices: {choices}, total cost: {total_cost}')
    save_logs('logcapbud.txt', capbudlogs, solution2)


if __name__ == '__main__':
    main()
