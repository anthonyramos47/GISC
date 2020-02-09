from Topologies import *
from Dynamics import *


def main():

    #redCompleta = network(20)
    #redCompleta.plot_ad_mat()
    
    # red  = swNet(25,4,0.5)
    # red.plot_ad_mat()
    # dyn = homophily( net=red, parameters=3, options=3, nach=1, T=100)
    # dyn.simulation("hom")

    red  = swNet(50,4,0.3)
    #red.plot_ad_mat()
    dyn = mass_media_two( net=red, parameters=5, options=4, nach=1, vec_B=[0.05, 0.08],  T=100)
    dyn.simulation("mass")
    




main()