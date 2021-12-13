import numpy as np

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
        Converts the list of node data into a list of stages made of Node objects
        """
        for idx, stage in enumerate(self.node_list):
            if idx == 0:
                # Make the first node
                self.stages.append([Node(stage[0], stage[1])])
            else:
                stage_list = []
                for node in stage:
                    stage_list.append(Node(node[0], node[1]))
                self.stages.append(stage_list)

        # Add a stage at the end representing the weights of 0 at the end
        self.stages.append([Node(0, 0, 0)] * (len(self.node_list) + 1))

    def cheapest_path(self):
        """
        Calculates the cheapest path through the network, saving the choices made in the node attributes.
        :return:
        """
        n = len(self.stages)
        for idx, stage in enumerate(reversed(self.stages)):
            for jdx, node in enumerate(stage):
                if idx == 0:
                    pass
                else:
                    # The weights of the connecting nodes. The complicated indices find the nodes depending on the
                    # current indices

                    dn_w = self.stages[n - idx][jdx + 1].weight
                    up_w = self.stages[n - idx][jdx].weight

                    if node.dn + dn_w > node.up + up_w:
                        node.choice = "up"
                        node.weight += node.up + up_w
                    else:
                        node.choice = "down"
                        node.weight += node.dn + dn_w

    def find_path(self):
        """
        Takes the calculated node list and traces the correct path, returning the choices made at each node in a list.
        :return: path, a list of choices made at each step.
        """
        init_choice = self.stages[0][0].choice
        rolling_i = 0 if init_choice == "up" else 1

        path = [init_choice]
        for idx,stage in enumerate(self.stages):
            if idx != 0 and idx != len(self.stages)-1:
                choice = stage[rolling_i].choice
                rolling_i += 1 if choice == "down" else 0
                path.append(choice)
        return path

    def solve_cheapest_path(self):
        self.def_nodes()
        self.cheapest_path()
        return self.find_path()