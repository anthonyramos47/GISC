from Node import node
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

class network():

    def __init__(self, NumeroNodos):
        """Constructor"""
        self.N = NumeroNodos
        self.nodes = self.completeGraph()
        

    def completeGraph(self):
        # Method that create a complete graph. It return a list of objects node.

    
    def adjacentMatrix(self):
        # Method to create the adjacent matrix of the
        # network. It return a list of list (matrix).


    def plot_ad_mat(self):
        # Method that plot the network. It return an
        # image of the topology of the network.
        N = self.N
        edges = []
        for i in range(N):
            cnx = self.nodes[i].cnx
            for j in cnx:
                edges.append([i,j])
        gr = nx.Graph() 
        # Initialize the graph
        gr.add_edges_from(edges)
        # Add the edges to graph
        nx.draw_circular(gr, node_size=250)
        # Define the characteristics of the plot
        #plt.savefig(file_name)
        plt.show() 

    def save_ad_mat(self, file_name):
        # Method that plot the network. It return an
        # image of the topology of the network.
        N = self.N
        edges = []
        for i in range(N):
            cnx = self.nodes[i].cnx
            for j in cnx:
                edges.append([i,j])
        gr = nx.Graph() 
        # Initialize the graph
        gr.add_edges_from(edges)
        # Add the edges to graph
        nx.draw_circular(gr, node_size=10)
        # Define the characteristics of the plot
        plt.savefig(file_name)
        #plt.show()

    def adjacentMatrixFile(self, fileName):
        # Method to export a file with the adjacent 
        # matrix. 
        # Input: Name of the file.
        # Return a file .dat with zeros and ones. 

        dataFile = open(str(fileName)+".dat","w")
        # Create the file 
        matrix = self.adjacentMatrix()  # Create the adjacent matrix
        totalN = self.N 
        for i in range(totalN):
            for j in range(totalN-1):
                dataFile.write("%d " % matrix[i][j])
            j +=1
            dataFile.write("%d" % matrix[i][j])
            dataFile.write("\n")
        # Write in the file the information of the adjacent matrix
        dataFile.close()
     

  
