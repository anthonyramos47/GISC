from Topologies import *
from Dynamics import *


def main():

    red  = swNet(10,4,0.5)
    dyn = homophile(red, 6, 3, 1, 10)

    print("Init Nodo1 :"+str(dyn.net_state.nodes[1].vec_Param))
    for t in range(10):
        dyn.homophile_step()
        print("time: {} Param  : {} \n".format(t, dyn.net_state.nodes[1].vec_Param))


main()