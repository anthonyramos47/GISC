# Module Homphile dynamics
from Topologies import *
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import random




class node_H:

    def __init__(self, vect, nach, cnxs):
        self.vec_Param = vect
        self.n_ach = nach # The number of attributes to change
        self.cnx = cnxs

class homophile:

    def __init__(self, net, parameters, options, nach, T):
        self.nodetype = node_H
        self.F = parameters
        self.Q = options
        self.n_ach = nach
        self.net_state = self.initializer(net)
        self.T = T

    def initializer(self, net):
        N = net.N #Total number of nodes
        for i in range(N):
            new_cnx = net.nodes[i].cnx
            parameters = self.parameters()
            net.nodes[i] = self.nodetype(parameters, self.n_ach, new_cnx)
        return net

    def parameters(self):
        opt = range(self.Q)
        total_elems = self.F
        vect = []
        for i in range(total_elems):
            vect.append(  random.choice(opt) )
        return vect


    def homophile_step(self):
        N=self.net_state.N
        for i in range(N):
            self.node_hom(i)
            
            
            

    def node_hom(self, i):
        n1=i
        n2=random.choice(self.net_state.nodes[n1].cnx)
   
        vec_sim= self.Sim(n1,n2)      #Obtener vector booleano. 1 equal. 0 diff.
        P=np.sum(vec_sim)/self.F   #probabilidad de interactuar
       
        if(random.random()<P):
            print("\n"+str(P))
            atrs_ch=select_atr(vec_sim, self.n_ach, self.F)  #Obtener lista de indices de atributos a cambiar
            
            print("Antes nodo:"+str(self.net_state.nodes[n1].vec_Param))
            for atr in atrs_ch:
                self.net_state.nodes[n1].vec_Param[atr]=self.net_state.nodes[n2].vec_Param[atr]
            print("Despues nodo:"+str(self.net_state.nodes[n1].vec_Param))

    def Sim(self, n1, n2):
        F= self.F
        vec_s=[]
        
        for i in range(F):
            if self.net_state.nodes[n1].vec_Param[i]==self.net_state.nodes[n2].vec_Param[i]:
                vec_s.append(1)
            else:
                vec_s.append(0)
        return vec_s

def select_atr(vec_sim, n_ach, F):
    atrs_ch = []

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
        