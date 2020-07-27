from Topologies import *
from Dynamics import *


def main():

    G = SmallWorldNetwork()
    G.create_graph(50,4,1)
    dyn = Two_Media(G, 2, 2, 0.5, 0.5, 1, 15)
    dyn.graph_click_simulation()


main()