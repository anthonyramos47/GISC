from topologies import SmallWorldNetwork, CompleteNetwork, SquareNetwork
from dynamics import TwoMedia


def main():
    
    
     #CN = CompleteNetwork(N = 4)
     #CN.draw_network()

     #SN = SquareNetwork(height = 4, width  = 3)
     #SN.draw_network()

     SWN = SmallWorldNetwork(N = 50,K = 5,p = 1)
     SWN.draw_network(with_labels = True)
    
     dyn = TwoMedia(SWN, 2, 2, 0.5, 0.5, 1, 15)
    #dyn.graph_click_simulation()


main()