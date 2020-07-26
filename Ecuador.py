from Node import node
from Network import network
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import random

                           
class Ecuador(network):
    def __init__(self):
        """Constructor"""
        self.N = 23
        self.nodes = self.completeGraph()
        self.positions = self.norm_positions()
    
    def load_positions(self):
        pos_file = open("posiciones.dat","r")
        position = []
        for line in pos_file:
            aux = line.split(" ")
            aux[0] = float(aux[0])
            aux[1] = float(aux[1])
            position.append( (aux[0], aux[1]) )
        return position

    def norm_positions(self):
        positions = self.load_positions()
        center = positions[1]
        angle = -np.pi/2.5
        norm_positions = [ ( np.cos(angle)*(- x[0] + center[0]) -  np.sin(angle)*(x[1]-center[1])  , np.sin(angle)*(- x[0] + center[0]) +  np.cos(angle)*(x[1]-center[1]) )for x in positions  ]
        #print(norm_positions)
        # fil = open("voronoi.dat","w")
        # for i in range(len(norm_positions)):
        #     fil.write(str(norm_positions[i][0])+"\t"+str(norm_positions[i][1]))
        #     fil.write("\n")
        # fil.close()
        return norm_positions

    def distance(self, positions, idx1, idx2 ):
        dist = ((positions[idx2][0] - positions[idx1][0])**2 + (positions[idx2][1] - positions[idx1][1])**2)**(1/2)
        return dist

    def max_dist(self, positions):
        N = len(positions)
        pos = []
        
        for i in range(N):
            j = i + 1
            while j > i and j < N:
                pos.append( self.distance(positions, i, j) )
                j = j + 1
        return max(pos)    

    def completeGraph(self):
        # Method that create a complete graph. It return a list of objects node.

        nodesList = [] # Create an empty list
        nodeT= self.N # Define the total number of nodes
        positions = self.load_positions()
        max_pos = self.max_dist(positions)
        for i in range(nodeT):
            nodesList.append( node([(x, self.distance(positions, x, i)/max_pos ) for x in range(nodeT)  if x != i])) 
        # Append an object node, that is connected with all the other nodes except itself, at each iteration
        return nodesList
        

    def printNodes(self):
        # Method to print the connections of all the nodes in the network
        for i in range(self.N):
            print("Nodo {}, {} ".format(i,self.nodes[i]))