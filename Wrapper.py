from Topologies import *
from Dynamics import *


def main():

    redCompleta = network(20)
    redCompleta.plotAdjacentMatrix()
    
    red  = swNet(25,4,0.5)
    red.plotAdjacentMatrix()
    dyn = homophily(red, 6, 3, 1, 10)
    dyn.simulation()




main()