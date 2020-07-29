import numpy as np
import matplotlib.pyplot as plt
import networkx as nx


class SquareNetwork(nx.Graph):
  def __init__(self, height, width ):
    """Define a square network with height x width nodes.
    """
    self.height = height
    self.width = width
    nx.Graph.__init__(self)  #import the attributes of the super class
    self.__create_graph()

  #Create the graph of the network given a height and width value
  def __create_graph(self):
    """Create a square graph with heigh x width nodes.
    """
    if (self.height < 2 or self.width < 2):
      print("INCORRECT: Set values of height or width >= 2")
      return

    self.clear() # Remove all the nodes and edges of the last graph
    current_node = 0
    for i in range(self.width):
      for j in range(self.height):  

          self.__adding_edges(i,j,current_node)

          #Adding neighbors to each node
          #Adding the node to the network
          #NOTE: Here if there are few attributes in a node, we can defined
          #the attributes in this part. So, we will use state=0 instead 
          #of data=node
          self.add_node(current_node, pos=(i,j)) 
          current_node +=1

  #Function to define the neihbors per node
  def __adding_edges(self,i,j,current_node):
    """Defines the neighbors of the current node"""
    #There are four possible connection
    directions = {
        "up" : current_node + 1,
        "down" : current_node - 1,
        "left" : current_node - self.height,
        "right" : current_node + self.height
    }

    #For border cases of the network, we have to pop some connections
    if i == 0:
      directions.pop("left")
    if i == self.width - 1:
      directions.pop("right")
    if j == 0:
      directions.pop("down")
    if j == self.height - 1:
      directions.pop("up")

    for _, neighbor in directions.items():
      self.add_edge(current_node, neighbor)


  #Function to plot the structure of the network
  def draw_network(self,node_color='blue', node_size=25, with_labels=False):
    """
    Draw the graph in a circular mode.
        
    node_size: the size of all the nodes
    node_color: the colo of all the nodes
    with_labels: True or False to show the ids of the nodes
    """
    pos = nx.get_node_attributes(self, 'pos')
    nx.draw(self, pos, node_color=node_color, node_size=node_size, with_labels=with_labels)
    plt.draw()
    plt.show()