from typing import Union
from BayesNet import BayesNet
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

var_set = (("bowel-problem", "family-out", "light-on", "dog-out", "hear-bark"),
           ("Winter?", "Sprinkler?", "Rain?", "Wet Grass?", "Slippery Road?"),
           ("I", "J", "Y", "X", "O"))
# print (nx.d_separated(bn_graph.bn.structure, {"bowel-problem"}, {"family-out"}, {"light-on"}))

def outnode(G, node):


def dsep(G, X, Y, Z):
    g = G.copy()

    # Start d-separation process:
    #

    # Step 1: Remove leaf nodes that are not in the given variables.
