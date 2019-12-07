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
        nodesList = []
        nodeT= self.N
        for i in range(nodeT):
            nodesList.append( node([x for x in range(nodeT)  if x != i]))
        return nodesList
    
    def adjacentMatrix(self):
        totalN = self.N
        matrix = np.zeros((totalN, totalN))
        for i in range(totalN):
            nodeaux = self.nodes[i]
            for j in nodeaux.cnx:
                matrix[i][j] = 1        
        return matrix

    def plotAdjacentMatrix(self):
        matrix = self.adjacentMatrix()
        rows, cols = np.where(matrix == 1) 
        edges = zip(rows.tolist(), cols.tolist())
        gr = nx.Graph()
        gr.add_edges_from(edges)
        nx.draw_circular(gr, node_size=10)
        plt.show() 

    def adjacentMatrixFile(self, fileName):
        dataFile = open(str(fileName)+".dat","w")
        matrix = self.adjacentMatrix()
        totalN = self.N
        for i in range(totalN):
            for j in range(totalN-1):
                dataFile.write("%d " % matrix[i][j])
            j +=1
            dataFile.write("%d" % matrix[i][j])
            dataFile.write("\n")
        dataFile.close()
     

  
