from Node import node
from Network import network
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import random


class nodeSW(node):
    
    def __init__(self, *argv):
        self.cnxL = argv[0]
        self.cnxR = argv[1]
        self.cnx = self.cnxL + self.cnxR

                       
class swNet(network):


    def __init__(self, NumeroNodos, K, p):
        """Constructor""" 
        self.N = NumeroNodos
        self.nodetype = nodeSW
        self.nodes = self.orderedNetwork(K)
        self.wsNet(p)
        

    def orderedNetwork(self, K):
        totalN = self.N
        nodesList = []
        for i in range(totalN):
            nodo = self.nodetype([],[])
            nodesList.append(self.vecinos(nodo, i, K))
        return nodesList

    def vecinos(self, nodo, i, K):
        totalN = self.N
        for j in range(K//2):
            nodo.cnxL.append((i-j-1)%totalN)
            nodo.cnxR.append((j+i+1)%totalN)
        self.actualizarcnx(nodo) 
        return nodo

    def actualizarcnx(self, nodo):
        nodo.cnx = nodo.cnxL + nodo.cnxR
        
        

    def printNodes(self):
        for i in range(self.N):
            print("Nodo {}, {} ".format(i,self.nodes[i]))



    def wsNet(self, p):
        #self.nodes() es una lista con los nodos
        
        N=self.N
        for i in range(N):
            rdm=random.random()
            if(rdm<p):
                n1=i #Actual
                n2=random.choice(self.nodes[n1].cnxR) #ex-coneccion
                n3=select_node(self.nodes[n1].cnx,n1,N) #Recableado 
                self.nodes[n1].cnxR.remove(n2)
                self.nodes[n1].cnx.remove(n2)
                self.nodes[n1].cnxL.append(n3)
                self.nodes[n1].cnx.append(n3)
          
                self.nodes[n2].cnxL.remove(n1)
                self.nodes[n2].cnx.remove(n1)
                
                self.nodes[n3].cnxL.append(n1)
                self.nodes[n3].cnx.append(n1)

def select_node(cnxs,n1,N):
    candidates=[]    
    for i in range(N):
        if (i not in cnxs) and (i != n1) :
            candidates.append(i)
    n2=random.choice(candidates)
    return n2

