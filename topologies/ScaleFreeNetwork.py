import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

class ScaleFreeNetwork(nx.Graph):
  def __init__(self, N , pre_created_graph = None):
    """Define a scale free network with N total number of nodes. 
      Also, you can provide a pre-created graph to add new nodes
      in the sense of a ScaleFree Network.
    """
    nx.Graph.__init__(self)  #import the attributes of the super class
    if (pre_created_graph is None):
      self.add_node(0)
      self.add_node(1)
      self.add_edge(0,1)
    else:
      self.add_nodes_from(pre_created_graph.nodes)
      self.add_edges_from(pre_created_graph.edges)

    self.N = N
    self.__create_graph()

  #Create the graph of the network given the N total number of nodes
  #This network starts from a graph with two connected nodes or a specific pre-created graph
  def __create_graph(self):
    """Create a scale-free graph with N nodes.
       The graph starts with some nodes, and continues adding 
       new nodes until get a total of N nodes. 
    """
    num_nodes = len(self.nodes)

    if (self.N <= num_nodes):
      print("INCORRECT: Set values of N > {0}".format(num_nodes))
      return


    for new_node in range(num_nodes,self.N):
        self.__adding_edges(new_node)

  def __adding_edges(self,new_node):
    """Defines the neighbors of the new node.Each node of the graph has a probability
          p = k_i / sum_k_j
       of being selected, where k_i is the connections of the i-node and
       cum_k_j is the cumulative connections of all the nodes of the graph. """


    sum_k_j = 0
    for node , _ in self.nodes.items():
      k_j = len(list(self.neighbors(node))) #the links of each node
      sum_k_j += k_j

    probabilities = []
    for node , _ in self.nodes.items():
      k_i = len(list(self.neighbors(node))) #the links of each node
      prob = k_i / sum_k_j
      probabilities.append(prob)

    # we use the np.random.choice function that selects a random number in the list
    # based on probabilities
    random_neighbor = np.random.choice(a=list(self.nodes), p=probabilities)
    
    self.add_edge(new_node,random_neighbor) 

  #Function to plot the structure of the network
  def draw_network(self,node_color='blue', node_size=25, with_labels=False):
    """
    Draw the graph.
        
    node_size: the size of all the nodes
    node_color: the coloe of all the nodes
    with_labels: True or False to show the ids of the nodes
    """
    nx.draw(self, node_color=node_color, node_size=node_size, with_labels=with_labels)
    plt.draw()
    plt.show()

    
    
    
