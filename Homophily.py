# Module Homphile dynamics
from Topologies import *
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import random


class Homophily():

    def __init__(self, graph, tot_par, tot_opt, n_ch, T):
        #Constructor of the homophily class
        # Inputs: 
        #   graph_type, the network topology
        #   graph_attrib, attributes requiere to create the network
        #   tot_par, the total number of parameters that each
        #       node have
        #   tot_opt, the total number of options that each
        #      parameter have
        #   n_ch, the number of attributes to change
        #   T, the total time that the dynamics will run
        self.graph = graph
        self.tot_par = tot_par
        self.tot_opt = tot_opt
        self.n_ch = n_ch
        self.T = T

    def graph_simulation(self):
        plt.ion()
        fig=plt.figure()
        self.add_nodes()
        for t in range(self.T):
            self.dynamic_step()
            self.draw_network()
            plt.show()
            plt.pause(0.001)

    def graph_click_simulation(self):
        self.add_nodes()
        fig =plt.figure()
        fig.canvas.mpl_connect('button_press_event', self.event_simulation )
        plt.show()
        plt.draw()

    def event_simulation(self, event):
        if event.button == 1:
            self.dynamic_step()
            self.draw_network()
            node_attrib = nx.get_node_attributes(self.graph, 'param')
            for k, v in node_attrib.items():
                print("Node : {0} with params: {1}".format(k, v))
        else:
            plt.close()


    def dynamic_step(self):
        N = self.graph.number_of_nodes()
        for i in range(N):
            self.node_dyn(i)
        self.set_colors()

    def add_nodes(self):
        # Method to add attributes to the nodes
        graph = self.graph
        opt = range(self.tot_opt)
        N = graph.number_of_nodes()
        dic = {}
        for i in range(N):
            vec_par = []
            for par in range(self.tot_par):
                vec_par.append(random.choice(opt))
            dic.update({ i: { 'param' : vec_par}})
        nx.set_node_attributes(graph, dic)

    def node_dyn(self, current_id):
        # Method tha implement the homophily dynamic 
        # per node
        # Input: current_id, index of the current node
        # Output: modified node i
        
        graph = self.graph
        nodes = graph.nodes()
        # Current node
        n1 = current_id
        # List of neighbors
        neigh_n1 = list(nx.neighbors(graph, n1))
        # Random neighbor of n1
        n2=random.choice(neigh_n1)
        
        # Parameters n1 and n2
        param_n1 = nodes[n1]['param']
        param_n2 = nodes[n2]['param']

        # Obtain a bool vector. 1 equal. 0 diff.   
        vec_sim= self.similarities(param_n1,param_n2)      

        # Interaction probability
        P = np.sum(vec_sim)/self.tot_par   
            
        if(random.random()<P):
            # Obtain the list of indeces of attributes to change
            atrs_ch=select_atr(vec_sim, self.n_ch, self.tot_par)  
            
            # Change the attributes of the node n1 as many times n_ch said    
            for atr in atrs_ch:
                param_n1[atr] = param_n2[atr]
                
            n1_update = {n1: {'param': param_n1}}
            nx.set_node_attributes(graph, n1_update)

    def similarities(self, param_n1, param_n2):
        # Method that create a boolean vector of 
        # similarities between attributes of n1 and n2
        # Input: n1, n2 indexes of the nodes
        # Output: vec_s, boolean vector
        
        # Initialization of the Similarity Vector
        vec_s=[]

        # Compute the similarities
        for i in range(self.tot_par):
            if param_n1[i] == param_n2[i]:
                vec_s.append(1)
            else:
                vec_s.append(0)
        return vec_s

    def n_base_transf(self, current_id):
        nodes = self.graph.nodes()
        base = self.tot_opt
        length = self.tot_par
        vec_param = nodes[current_id]['param']
        sumation = 0
        for i in range(length):
            sumation += base**i * vec_param[i]
        return sumation
    
    def set_colors(self):
        base = self.tot_opt
        length = self.tot_par
        N = self.graph.number_of_nodes()
        nodes = self.graph.nodes()
        step = 1/(base**length)
        val_map = lambda i:  step*i 
        for nd in range(N):
            col_nd = val_map(self.n_base_transf(nd))
            nodes[nd]['color'] = col_nd
    
    #Function to plot the structure of the network
    def draw_network(self):
        plt.clf()
        graph = self.graph
        N = graph.number_of_nodes()
        nodes = graph.nodes()
        lst_nodes = list(graph.nodes())
        colormap = plt.get_cmap('plasma')
        colors = [colormap(nodes[i]['color']) for i in lst_nodes]
        pos = nx.get_node_attributes(self.graph, 'pos')
        if pos =={}:
            nx.draw_circular(graph, node_size=250, with_labels=True, node_color=colors)
        else:
            nx.draw(graph, pos, node_size=250, with_labels=True, node_color=colors)
        plt.draw()
        #plt.show()

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