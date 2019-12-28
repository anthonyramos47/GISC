# Module Homphile dynamics
from Topologies import *
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import random




class node_H:

    def __init__(self, vect, cnxs):
        # Constructor of the node used in the
        # homophily dynamics
        # Inputs: vec_Param, a list of integers
        #         cnx, the list of neighbors
        self.vec_Param = vect
        self.cnx = cnxs 
        # List of neighbors of type node_H

class homophily:

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

        self.nodetype = node_H
        self.F = parameters
        self.Q = options
        self.n_ach = nach
        self.net_state = self.initializer(net)
        self.T = T

    def initializer(self, net):
        # Method that given a network with an arbitrary
        # topology it change the type of node. 
        # Input: net, a network with arbitrary topology
        # Output: the same network with different types 
        # or class of node. 

        N = net.N 
        #Total number of nodes
        for i in range(N):
            new_cnx = net.nodes[i].cnx
            parameters = self.parameters()
            # Generate the vector of parameter for each
            # node
            net.nodes[i] = self.nodetype(parameters, new_cnx)
            # modify the type of node in the network
        return net

    def parameters(self):
        # Method to randomly generate the vector of 
        # parameters of the nodes. 
        # Output: vect, a list of parameters of length
        # F with integers between [0,Q-1]
        opt = range(self.Q)
        total_elems = self.F
        vect = []
        for i in range(total_elems):
            vect.append(  random.choice(opt) )
        return vect


    def homophily_step(self):
        # Method tha apply the homophile dynamics for 
        # all the nodes of the network
        # Output: modifies the self.net_state
        N=self.net_state.N
        for i in range(N):
            self.node_hom(i)
            
            
            

    def node_hom(self, i):
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
        # Output: bec_s, boolean vector
        F= self.F
        vec_s=[]
        
        for i in range(F):
            if self.net_state.nodes[n1].vec_Param[i]==self.net_state.nodes[n2].vec_Param[i]:
                vec_s.append(1)
            else:
                vec_s.append(0)
        return vec_s

    def simulation(self):
        # Method that run a complet simulation of 
        # homophily dynamics with time T

        T_total = self.T

        for t in range(T_total):
            self.homophily_step()
            #print("time: {} Param  : {} \n".format(t, self.net_state.nodes[1].vec_Param))


def select_atr(vec_sim, n_ach, F):
    atrs_ch = []
    # Function to obtain the indixes of the attributes
    # to change
    not_eq= F-np.sum(vec_sim)
    if n_ach > not_eq:
        n_ach=not_eq
    
    candidates=[]
    
    for i in range(len(vec_sim)):
        if vec_sim[i]==0:
            candidates.append(i)
    
    for i in range(n_ach):
        selec=random.choice(candidates)
        atrs_ch.append(selec)
        candidates.remove(selec)
        
    return atrs_ch
        