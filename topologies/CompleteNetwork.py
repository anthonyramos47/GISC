import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

class CompleteNetwork(nx.Graph):
    def __init__(self, N):
        """Define a complete network with N nodes.
        A complete network is a network where the nodes are connected all with all
        """
        self.N = N
        nx.Graph.__init__(self)  #import the attributes of the super class
        self.__create_graph()

  #Create the graph of the network given N nodes
    def __create_graph(self):
        """Create a complete graph with N nodes.
        """
        if (self.N < 3):
            "INCORRECT: Set correct number of nodes >= 3"
            return

        self.clear()
        for i in range(self.N):
            self.__adding_edges(i)
            #Adding the node to the network
            self.add_node(i) 

    #Function to define the neighbors per node
    def __adding_edges(self,current_node):
        """Defines the neighbors of the current node"""
        neighbors = [x for x in range(self.N)  if x != current_node]

        for neighbor in neighbors:
            self.add_edge(current_node, neighbor)


    #Function to plot the structure of the network
    def draw_network(self, node_color='blue', node_size=25, with_labels=False):
        """
        Draw the graph in a circular mode.
        
        node_size: the size of all the nodes
        node_color: the colo of all the nodes
        with_labels: True or False to show the ids of the nodes
        """
        nx.draw_circular(self, node_color=node_color, node_size=node_size, with_labels=with_labels)
        plt.draw()
        plt.show()




# class network():

#     def __init__(self, NumeroNodos):
#         """Constructor"""
#         self.N = NumeroNodos
#         self.nodes = self.completeGraph()
        

#     def completeGraph(self):
#         # Method that create a complete graph. It return a list of objects node.

#         nodesList = [] # Create an empty list
#         nodeT= self.N # Define the total number of nodes
#         for i in range(nodeT):
#             nodesList.append( node([x for x in range(nodeT)  if x != i])) 
#         # Append an object node, that is connected with all the other nodes except itself, at each iteration
#         return nodesList
    
#     def adjacentMatrix(self):
#         # Method to create the adjacent matrix of the
#         # network. It return a list of list (matrix).

#         totalN = self.N # Total number of nodes
#         matrix = np.zeros((totalN, totalN)) 
#         # Initialize a matrix N x N of zeros
#         for i in range(totalN):
#             nodeaux = self.nodes[i]
#             for j in nodeaux.cnx:
#                 matrix[i][j] = 1      
#         # For each node i, at j an integer in the list 
#         # of connections of the node it is put a 1 in 
#         # the position matrix[i,j] s
#         return matrix

#     def plot_ad_mat(self):
#         # Method that plot the network. It return an
#         # image of the topology of the network.
#         N = self.N
#         edges = []
#         for i in range(N):
#             cnx = self.nodes[i].cnx
#             for j in cnx:
#                 edges.append([i,j])
#         gr = nx.Graph() 
#         # Initialize the graph
#         gr.add_edges_from(edges)
#         # Add the edges to graph
#         nx.draw_circular(gr, node_size=250)
#         # Define the characteristics of the plot
#         #plt.savefig(file_name)
#         plt.show() 

#     def save_ad_mat(self, file_name):
#         # Method that plot the network. It return an
#         # image of the topology of the network.
#         N = self.N
#         edges = []
#         for i in range(N):
#             cnx = self.nodes[i].cnx
#             for j in cnx:
#                 edges.append([i,j])
#         gr = nx.Graph() 
#         # Initialize the graph
#         gr.add_edges_from(edges)
#         # Add the edges to graph
#         nx.draw_circular(gr, node_size=10)
#         # Define the characteristics of the plot
#         plt.savefig(file_name)
#         #plt.show()

#     def adjacentMatrixFile(self, fileName):
#         # Method to export a file with the adjacent 
#         # matrix. 
#         # Input: Name of the file.
#         # Return a file .dat with zeros and ones. 

#         dataFile = open(str(fileName)+".dat","w")
#         # Create the file 
#         matrix = self.adjacentMatrix()  # Create the adjacent matrix
#         totalN = self.N 
#         for i in range(totalN):
#             for j in range(totalN-1):
#                 dataFile.write("%d " % matrix[i][j])
#             j +=1
#             dataFile.write("%d" % matrix[i][j])
#             dataFile.write("\n")
#         # Write in the file the information of the adjacent matrix
#         dataFile.close()
     

  