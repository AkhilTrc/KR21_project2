from typing import Union
from BayesNet import BayesNet
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt


class BNReasoner:
    def __init__(self, net: Union[str, BayesNet]):
        """
        :param net: either file path of the bayesian network in BIFXML format or BayesNet object
        """
        if type(net) == str:
            # constructs a BN object
            self.bn = BayesNet()
            # Loads the BN from an BIFXML file
            self.bn.load_from_bifxml(net)
        else:
            self.bn = net

    # TODO: This is where your methods should go

bn_graph = BNReasoner("testing/dog_problem.BIFXML")

X, Y, Z = "bowel-problem", "light-on", "family-out"

print (f"Is {X} d-separated from {Y} by {Z}? ", dsep(bn_graph, X, Y, Z))

var_set = (("bowel-problem", "family-out", "light-on", "dog-out", "hear-bark"),
           ("Winter?", "Sprinkler?", "Rain?", "Wet Grass?", "Slippery Road?"),
           ("I", "J", "Y", "X", "O"))
# print (nx.d_separated(bn_graph.bn.structure, {"bowel-problem"}, {"family-out"}, {"light-on"}))

def dsep(G, X, Y, Z):
    g = G.bn.copy()
    XYZ = X.union(Y).union(Z)

    # Find and remove leaf nodes that are not part of the x, y, z union.
    #
    l_nodes = deque()
    for node in g.nodes:
        if g.out_degree[node] == 0:     # Finds all the leaf nodes.
            l_nodes.append(node)
    while len(l_nodes) > 0:
        l = l_nodes.popleft()
        if l not in XYZ:
            # need a way to add parent to l.
            g.bn.del_var(l)

    g.remove_edges_from(g.out_edge(Z))  # Removes all edges outgoing from nodes in Z.

    if d-separated:  ############################################
        return True
    else:
        return False


