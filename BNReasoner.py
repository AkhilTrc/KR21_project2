from typing import Union
from BayesNet import BayesNet
import networkx as nx   #####################################
import matplotlib.pyplot as plt #################################


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
bn_graph = BNReasoner("testing/dog_problem.BIFXML")     # creates object bn_graph

# print (bn_graph.bn.get_all_variables())
# print (bn_graph.bn.get_children("family-out"))
# print (bn_graph.bn.get_cpt("family-out"))
# print (bn_graph.bn.get_all_cpts())
# print (bn_graph.bn.get_interaction_graph())

# nx.draw(bn_graph.bn.get_interaction_graph(), with_labels=True, node_size=3000)
# plt.show()

bn_graph.bn.draw_structure()

