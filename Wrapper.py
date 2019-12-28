from Topologies import *
from Dynamics import *


def main():

    #redCompleta = network(20)
    #redCompleta.plotAdjacentMatrix()
    
    red  = swNet(10,4,0.5)
    dyn = homophily(red, 6, 3, 1, 10)

    dyn.simulation()


main()