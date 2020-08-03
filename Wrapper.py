from topologies import SmallWorldNetwork, CompleteNetwork, SquareNetwork, ScaleFreeNetwork
from dynamics import TwoMedia, Homophily


def main():
    
    
     #CN = CompleteNetwork(N = 4)
     #CN.draw_network()

     SN = SquareNetwork(height = 5, width  = 5)
     #SN.draw_network()

     #SFN = ScaleFreeNetwork(100)
     #SFN.draw_network()

     #SWN = SmallWorldNetwork(N = 50,K = 5,p = 1)
     #SWN.draw_network(with_labels = True)
     
     dyn = Homophily(graph=SN, tot_par = 3, tot_opt =2, n_ch=1, T=10)
     dyn.graph_click_simulation()


main()