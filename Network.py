import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

class Network(nx.Graph):
    def __init__(self, nodes = None):
        nx.Graph.__init__(self)  #import the attributes of the super class

  #Create the graph of the network given a height and width value
    def create_graph(self, N):
        for i in range(N):
            self.__adding_edges(i, N)
            #Adding the node to the network
            #NOTE: Here if there are few attributes in a node, we can defined
            #the attributes in this part. So, we will use state=0 instead 
            #of data=node
            self.add_node(i) 

    #Function to define the neihbors per node
    def __adding_edges(self,current_id, totalN):
        neigh = [x for x in range(totalN)  if x != current_id]

        for id in neigh:
            self.add_edge(current_id, id)


    #Function to plot the structure of the network
    def draw_network(self):
        nx.draw_circular(self, node_color='blue', node_size=25, with_labels=False)
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
     

  