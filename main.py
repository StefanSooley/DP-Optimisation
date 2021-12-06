from recursion import Node, Graph
import numpy as np

def main():
    nodes = np.array([[2, 1], [[2, 3], [3, 2]]], dtype='object')
    g = Graph(nodes)
    g.def_nodes()
    g.cheapest_path()
    g.find_path()

if __name__ == '__main__':
    main()