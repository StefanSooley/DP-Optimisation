import numpy as np

# nodes = np.array([[2, 1], [[2, 3], [3, 2]]], dtype='object')

class Node:
    def __init__(self, up, dn, weight=0):
        self.weight = weight
        self.up = up
        self.dn = dn



class Stage:
    def __init__(self, nodes):
        self.nodes = nodes


class Graph:
    def __init__(self, node_list):
        self.node_list = node_list
        self.stages = []

    def build_graph(self):
        for stage in self.node_list:

            self.stages.append([])



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