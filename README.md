# GISC

This project shows some `topologies` and `dynamics` of small world networks for research purposes. This project used the library [Networkx](https://networkx.github.io/) to facilitate the use and observation of graphs.
Also, it was added some notebooks in the `Documentation` folder for understanding each part of the project.

## How to explore the project

### Topologies 

The implemented topologies are `CompleteNetwork`, `ScaleFreeNetwork`, `SquareNetwork`, and `SmallWorldNetwork`. You can find the class definitions on the folder `topologies`.

- **Complete Network.** It is a network with `N` where each node is linked with all other nodes.
- **Square Network.** This topology is also known as Lattice. It is a network where the nodes are placed in mesh structure defined by `width` and `height`. Thus, each node has at most 4 neighbors. 
- **Scale Free Network.** It is a network constructed by progressively adding nodes to an existing network and introducing links to existing nodes with preferential attachment so that the probability of linking to a given node *i* is proportional to the number of existing links *k_i* that node has, i.e.
<img alt="centered image" src="https://render.githubusercontent.com/render/math?math=P(\text{linking to node i}) \sim \frac{k_i}{\sum_j k_j}">

- **Small World Network.** This network is made in two phases where the network goes through an ordered network to a disordered network, but always conserving the level of connection. Thus, the following parameter defines the structure of the network:
	* `N` = number of total nodes
	* `K` = neighbors of each node in the first ordered graph. Average links number.
	* `p` = disorder probability or disorder level.

### Dynamic

- **Homophily** This dynamic consider a network G, where each node has a state vector  <img alt="bottom image" src="https://render.githubusercontent.com/render/math?math=C_i">  with length F and each element of <img alt="bottom image" src="https://render.githubusercontent.com/render/math?math=\sigma_{ij} \in C_i"> has q possible choices. In each stept of the dynamics, it is choose a random neighbor  <img alt="bottom image" src="https://render.githubusercontent.com/render/math?math=n_j \in G">   of a node <img alt="bottom image" src="https://render.githubusercontent.com/render/math?math=n_i \in G">  and in dependence of how similar are the state vectors a given number of elements (n_ch) of <img alt="bottom image" src="https://render.githubusercontent.com/render/math?math=C_j">  are copied to <img alt="bottom image" src="https://render.githubusercontent.com/render/math?math=C_i">. This mimic the homophily in social terms https://en.wikipedia.org/wiki/Homophily.
