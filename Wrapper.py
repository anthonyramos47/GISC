from Topologies import *
from Dynamics import *


def main():

    #redCompleta = network(20)
    #redCompleta.plot_ad_mat()
    
    # red  = swNet(25,4,0.5)
    # red.plot_ad_mat()
    # dyn = homophily( net=red, parameters=3, options=3, nach=1, T=100)
    # dyn.simulation("hom")

    # red  = swNet(50,4,0.3)
    # red.plot_ad_mat()
    # dyn = mass_media_two( net=red, parameters=5, options=4, # # nach=1, vec_B=[0.05, 0.08],  T=100)
    # dyn.simulation("mass")
    # (self, net, T, k, b, rq, q, qv, p, death_rates, recovery_rates, detection_rates):
    redEc = Ecuador()
    cor_dyn = corona(redEc, 100, 10, 0.7, 1/20, 0.5, 0.02, 1/7, [0.000911186, 0.000911186, 0.000911186, 0.000911186, 0.000911186], [0.0000803988, 0.0000803988, 0.0000803988], [0.4, 0.3])
    cor_dyn.insert_infected(0, 1)
    cor_dyn.insert_latent(0, 1)
    cor_dyn.initial_cond()
    cor_dyn.simulation("corona")
    
    #print(ord_provinces("natalidad.dat"))




main()