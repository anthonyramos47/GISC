import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import random


class SmallWorldNetwork(nx.Graph):
    def __init__(self, nodes = None):
        nx.Graph.__init__(self)  #import the attributes of the super class

  #Create the graph of the network given a height and width value
    def create_graph(self, N, K, p):
        self.clear() 
        self.small_world_net(N, K, p)

    def small_world_net(self, N, K, p):
        self.ordered_network(N, K)
        #scram_Edges = []
        for node in range(N):
            list_neighbors = [n for n in self.neighbors(node)]+[node]
            rewired_nodes = []
            for neigh in range(node+1, node+K//2+1):
                rdm=random.random()
                # Get a random number between [0-1]
                if(rdm<p):
                    self.remove_edge(node, neigh%N)
                    # list_edges = [ele for tup in scram_Edges for ele in tup]
                    candidates = [x for x in range(N) if x not in list_neighbors and x not in rewired_nodes ]
                   # print('Node:', node, 'Candidates', candidates)
                    new_neigh = random.choice(candidates)
                  #  print('Node:', node, 'NewNode:', new_neigh)
                    self.add_edge(node, new_neigh)
                    rewired_nodes.append(new_neigh)

    def ordered_network(self, N, K):
        for i in range(N):
            self.__adding_edges(i, N, K)
            self.add_node(i)

    #Function to define the neihbors per node
    def __adding_edges(self,current_id, totalN, K):
        neigh  = []
        for j in range(K//2):
            neigh.append((current_id-j-1)%totalN)
            neigh.append((j+current_id+1)%totalN)

        for id in neigh:
            self.add_edge(current_id, id)


    #Function to plot the structure of the network
    def draw_network(self, col):
        nx.draw_circular(self, node_color=col, node_size=25, with_labels=True)
        plt.draw()
        plt.show()


# class nodeSW(node):
    
#     def __init__(self, *argv):
#         #Constructor of the node used in the Small world network algorithm. The right connections correspond to those that we are going to reconnect. The left connections correspond to those that are going to be eliminated.

#         self.cnxL = argv[0]
#         # Left connections 
#         self.cnxR = argv[1]
#         # Right connections 
#         node.__init__(self, self.cnxL + self.cnxR)
#         # Total connections 

                       
# class swNet(network):


#     def __init__(self, NumeroNodos, K, p):
#         """Constructor""" 
#         self.N = NumeroNodos
#         # Total Number of nodes
#         self.nodetype = nodeSW
#         # Type of node of the network
#         self.nodes = self.orderedNetwork(K)
#         # Create a ordered network
#         self.wsNet(p)
#         # Scramble the network 
#         # #with a probability p
        

#     def orderedNetwork(self, K):
#         # Method to create an ordered network with
#         # K number of neighbors per node
#         # Input: K, number of neighbors
#         # Outputs: List of objects self.nodetype

#         totalN = self.N
#         # total number of nodes
#         nodesList = []
#         # Initialice an empty list
#         for i in range(totalN):
#             nodo = self.nodetype([],[])
#             nodesList.append(self.vecinos(nodo, i, K))
#         # Append a class node with k neighbors; k/2 to left, k/2 to the right
#         return nodesList

    # def vecinos(self, nodo, i, K):
    #     # Method to assing the neigbors to a node
    #     # Input: nodo, class node
    #     #        i, the position of the node
    #     #        K, the total number of neighbors
    #     # Outputs: object self.typenode
                           
    #     totalN = self.N
    #     for j in range(K//2):
    #         nodo.cnxL.append((i-j-1)%totalN)
    #         # Assign the left connections
    #         nodo.cnxR.append((j+i+1)%totalN)
    #         # Assign the right connections
    #     self.actualizarcnx(nodo)
    #     # Update the state of the node 
    #     return nodo

#     def actualizarcnx(self, nodo):
#         # Method to update the total connections 
#         # of a node
#         # Input: object node
#         nodo.cnx = nodo.cnxL + nodo.cnxR
        
        

#     def printNodes(self):
#         # Method to print the connections of all the nodes in the network
#         for i in range(self.N):
#             print("Nodo {}, {} ".format(i,self.nodes[i]))



#     def wsNet(self, p):
#         # Method to scramble an orderned network
#         # with probability p
#         # Input: p, float 
#         # Output: updated network
        
#         N=self.N
#         # Total number of nodes
#         for i in range(N):
#         # We go through the network in counterclockwise direction, namely the from 0 to N. We assume that we had a circular network representation.
#             rdm=random.random()
#             # Get a random number between [0-1]
#             if(rdm<p):
#             # Verify if the random number is less than p
#                 n1=i 
#                 # Actual node
#                 n2=random.choice(self.nodes[n1].cnxR) 
#                 # Randomly we choose a connection to 
#                 # elminate
#                 n3=select_node(self.nodes[n1].cnx,n1,N) 
#                 # Randomly we choose a new connection

#                 self.nodes[n1].cnxR.remove(n2)
#                 #self.nodes[n1].cnx.remove(n2)
#                 # Remove the connection n2 from n1
#                 self.nodes[n1].cnxL.append(n3)
#                 #self.nodes[n1].cnx.append(n3)
#                 # Add the new connection n3 to n1
          
#                 self.nodes[n2].cnxL.remove(n1)
#                 #self.nodes[n2].cnx.remove(n1)
#                 # Remove the node n1 from 
#                 # the connections of  n2
                
#                 self.nodes[n3].cnxL.append(n1)
#                 #self.nodes[n3].cnx.append(n1)
#                 # Add the node n1 to n3
#                 self.actualizarcnx(self.nodes[n1])
#                 self.actualizarcnx(self.nodes[n2])
#                 self.actualizarcnx(self.nodes[n3])

# def select_node(cnxs,n1,N):
#     # Function to choose a random node
#     candidates=[]    
#     for i in range(N):
#         if (i not in cnxs) and (i != n1) :
#             candidates.append(i)
#     n2=random.choice(candidates)
#     return n2

