# Module Homphile dynamics
from Topologies import *
from Node import node
from genDynamics import *
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import random


class node_H(node_D):

    def __init__(self, vect, cnxs):
        # Constructor of the node used in the
        # homophily dynamics
        # Inputs: vec_Param, a list of integers
        #         cnx, the list of neighbors
        node_D.__init__(self, vect, cnxs)
        # List of neighbors of type node_H

class homophily(dynamics):

    def __init__(self, net, parameters, options, nach, T):
        #Constructor of the homophily class
        # Inputs: 
        #   nodetype, specifies the type of node that 
        #             it is used
        #   F, the total number of parameters that each
        #       node have
        #   Q, the total number of options that each
        #      parameter have
        #   n_ach, the number of attributes to change
        #   net_state, is the state of the network at a #              given time
        #   T, the total time that the dynamics will run
        dynamics.__init__(self, net, parameters, options, nach, T)

    

    def node_dyn(self, i):
        # Method tha implement the homophily dynamic 
        # per node
        # Input: i, index of the node
        # Output: modified node i
        
        n1=i 
        # node i
        n2=random.choice(self.net_state.nodes[n1].cnx)
        # Random neighbor of n1
   
        vec_sim= self.similarities(n1,n2)      
        # Obtain a bool vector. 1 equal. 0 diff.
        P=np.sum(vec_sim)/self.F   
        # Interaction probability
       
        if(random.random()<P):
           
            atrs_ch=select_atr(vec_sim, self.n_ach, self.F)  
            # Obtain the list of indeces of attributes to change
            
            for atr in atrs_ch:
            # Change the attributes of the node n1 as many times n_ach said    
                self.net_state.nodes[n1].vec_Param[atr]=self.net_state.nodes[n2].vec_Param[atr]
            

    def similarities(self, n1, n2):
        # Method that create a boolean vector of 
        # similarities between attributes of n1 and n2
        # Input: n1, n2 indexes of the nodes
        # Output: vec_s, boolean vector
        F = self.F 
        # Number of attributes
        vec_s=[]
        
        for i in range(F):
            if self.net_state.nodes[n1].vec_Param[i]==self.net_state.nodes[n2].vec_Param[i]:
                vec_s.append(1)
            else:
                vec_s.append(0)
        return vec_s

