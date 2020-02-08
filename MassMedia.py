# Module Mass Media dynamics
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

class mass_media(dynamics):

    def __init__(self, net, parameters, options, nach, B, T):
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
        self.B = B
        self.media = self.parameters()
         

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

    def dynamic_step(self):
        # Method tha apply the homophile dynamics for 
        # all the nodes of the network
        # Output: modifies the self.net_state
        N=self.net_state.N
        for i in range(N):
            self.node_dyn(i)

    def node_dyn(self, i):
        # Method tha implement the homophily dynamic 
        # per node
        # Input: i, index of the node
        # Output: modified node i
        
        n1=i 
        # node i

        if (random.random() < self.B):

            vec_simM = self.simMassMedia(n1)
            Pm = P=np.sum(vec_simM)/self.F   
            # Interaction probability
        
            if(random.random() < Pm):
            
                atrs_ch=select_atr(vec_simM, self.n_ach, self.F)  
                # Obtain the list of indeces of attributes to change
                
                for atr in atrs_ch:
                # Change the attributes of the node n1 as many times n_ach said    
                    self.net_state.nodes[n1].vec_Param[atr]=self.media[atr]
                
        else:

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
                

    def simMassMedia(self, n1):
        # Method that create a boolean vector of 
        # similarities between attributes of n1 and n2
        # Input: n1, n2 indexes of the nodes
        # Output: vec_s, boolean vector
        F = self.F 
        # Number of attributes
        vec_s=[]
        
        for i in range(F):
            if self.net_state.nodes[n1].vec_Param[i]==self.media[i]:
                vec_s.append(1)
            else:
                vec_s.append(0)
        return vec_s

    def simulation(self, file_name):
        # Method that run a complet simulation of 
        # homophily dynamics with time T

        T_total = self.T
        print(self.media)
        print(self.color_media())
        
        for t in range(T_total):
            self.dynamic_step()
            self.save_color_media(file_name+str(t))
            
            self.print_states(file_name+str(t))
            #print("time: {} Param  : {} \n".format(t, self.net_state.nodes[1].vec_Param))

    def save_color_media(self, file_name):
        # Method that plot the network. It return an
        # image of the topology of the network.
        N = self.net_state.N
        edges = []
        for i in range(N):
            cnx = self.net_state.nodes[i].cnx
            for j in cnx: 
                edges.append([i,j])
        gr = nx.Graph() 
        gr2 = nx.Graph() 
        # Initialize the graph
        gr.add_edges_from(edges)
        # Add the edges to graph
        colors = self.coloring_val(gr)
        
        gr2.add_node("Media", pos=(1,1), node_size=800 )
        
        colormap=plt.get_cmap('plasma')
        
        nx.draw_circular(gr, cmap=plt.get_cmap('plasma'), node_color=colors, with_labels=True, node_size=250, font_color='black')
        position = nx.get_node_attributes(gr2,'pos')
        print(self.color_media())
        nx.draw(gr2, pos= position,
        node_color= colormap(self.color_media()) , with_labels=True, node_size=1500, font_color='black')
        # Define the characteristics of the plot
        plt.savefig(file_name)
        #plt.show()   

    def coloring_val(self, graph):
        base = self.Q
        length = self.F
        nodes = self.net_state.nodes
        step = 1/(base**length)
        val_map = lambda i:  step*i 
        values = [val_map(self.n_base_transf(nodes[node])) for node in graph.nodes()]
        return values

    def color_media(self):
        base = self.Q
        length = self.F
        step = 1/(base**length)
        val_map = lambda i:  step*i 
        value = val_map(self.n_base_mass())
        return value

    def n_base_mass(self):
        base = self.Q
        length = self.F 
        sumation = 0
        media = self.media
        for i in range(length):
            sumation += base**i * media[i]
        return sumation
