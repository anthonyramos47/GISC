import numpy as np
import matplotlib.pyplot as plt
import networkx as nx



class SquareNetwork(nx.Graph):
  def __init__(self, nodes = None):
    nx.Graph.__init__(self)  #import the attributes of the super class

  #Create the graph of the network given a height and width value
  def create_graph(self, height, width):
    if (height < 2 or width < 2):
      print("INCORRECT: Set values of height or width >= 2")
      return

    self.clear() # Remove all the nodes and edges of the last graph
    counter = 0
    for i in range(width):
      for j in range(height):  

          self.__adding_edges(i,j,counter,height,width)

          #Adding neighbors to each node
          #Adding the node to the network
          #NOTE: Here if there are few attributes in a node, we can defined
          #the attributes in this part. So, we will use state=0 instead 
          #of data=node
          self.add_node(counter, pos=(i,j)) 
          counter +=1

  #Function to define the neihbors per node
  def __adding_edges(self,i,j,current_id, height, width):
    
    #There are four possible connection
    directions = {
        "up" : current_id + 1,
        "down" : current_id - 1,
        "left" : current_id - height,
        "right" : current_id + height
    }

    #For border cases of the network, we have to pop some connections
    if i == 0:
      directions.pop("left")
    if i == width - 1:
      directions.pop("right")
    if j == 0:
      directions.pop("down")
    if j == height - 1:
      directions.pop("up")

    for k, v in directions.items():
      self.add_edge(current_id, v)


  #Function to plot the structure of the network
  def draw_network(self):
    pos = nx.get_node_attributes(self, 'pos')
    nx.draw(self, pos, node_color='blue', node_size=25, with_labels=False)
    plt.draw()
    plt.show()