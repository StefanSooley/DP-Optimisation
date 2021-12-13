from recursion import Node, Graph
import numpy as np


def main():
    nodes = np.array([[2, 1], [[2, 3], [3, 2]], [[2, 3], [6, 2], [4, 5]], [[3, 4], [5, 1], [2, 3], [3, 4]]],
                     dtype='object')
    g = Graph(nodes)
    sol = g.solve_cheapest_path()
    print(sol)


if __name__ == '__main__':
    main()
