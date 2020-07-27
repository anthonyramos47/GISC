# Module Homphile dynamics
from Topologies import *
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import random


class province():

    def __init__(self, pop, cnx, mu, birth):
        # Constructor of the province
        # Input:
        self.pop = pop # Population
        self.cnx = cnx # List of  Weight Connections (id, weight)
        self.time = 0 # Time step (days)
        self.iu = 0  # Infected Undetected
        self.id = 0 # Infected Isolated
        self.iq = 0 # Infected Quarantined
        self.latent = 0 # Infected Latent
        self.latentQ = 0 # Infected Latent Quarantined
        self.sus = 0 # Susceptible 
        self.susQ = 0 # Susceptible Quarantined
        self.death = 0 
        self.death_nat = 0 
        self.rec = 0 
        self.time = 0
        self.birth = birth
        self.mu = mu 
        self.migr = 1 #Probability of migration per province
   
        

class corona(dynamics):

    def __init__(self, net, T, k, b, rq, q, qv, p, death_rates, recovery_rates, detection_rates):
        #Constructor of the homophily class
        # Inputs: 
        #   nodetype,- specifies the type of node that 
        #             it is used
        #   quaantine,- list of nodes in quarantine
        #   T, the total time that the dynamics will run
        #   k, baseline daily number of contact
        #   b, probability of transmition
        #   v, recovery rate 
        #   m, probability of death 
        #   w, porcentage of effective isolation
        #  1/p, mean time from progression from latently to infectious
        #  1/rq, Duration of Quarantine
        self.k  = k 
        self.b = b
        self.rq = rq
        self.q = q 
        self.p = p
        self.qvol = qv
        self.xmu = death_rates[0]
        self.emu = death_rates[1]
        self.iumu = death_rates[2]
        self.idmu = death_rates[3]
        self.iqmu = death_rates[4]
        self.riu =  recovery_rates[0]
        self.riq =  recovery_rates[1]
        self.rid = recovery_rates[2]
        self.diu = detection_rates[0]
        self.diq = detection_rates[1]
        self.nodetype = province
        self.net_state = self.initializer(net)
        self.T = T

    def initializer(self, net):
        # Method that given a network with an arbitrary
        # topology it change the type of node. 
        # Input: net, a network with arbitrary topology
        # Output: the same network with different types 
        # or class of node. 
        N = net.N 
        pop_file = open("population.dat","r")
        pop_data = []
        for line in pop_file:
            pop_data.append( int(line[:-1]) )
        death_rates = ord_provinces("muerte.dat")
        birth_rates = ord_provinces("natalidad.dat")
        for i in range(N):
            new_cnx = net.nodes[i].cnx
            # Recall the conections from the stablished topology
            net.nodes[i] = self.nodetype(pop= pop_data[i], cnx=new_cnx, mu=death_rates[i], birth= birth_rates[i])
            # modify the type of node in the network
        return net


    def initial_cond(self):
        # Method that stablish the initial population 
        # for the susceptible and susceptible quarantined
        nodes =self.net_state.nodes 
        tot = self.net_state.N
        for i in range(tot):
            province = nodes[i] # Select the province
            n0 = province.pop # Define the n0
            province.sus = n0*0.7 
            province.susQ = n0*0.3

    def dynamic_step(self):
        # Method tha implement the dynamic for SARS desease 
        # for node
        # Output: modifies the self.net_state

        # Define the variables used in the dynamical
        # system
        nodes = self.net_state.nodes
        total_nodes = self.net_state.N
        k = self.k
        b = self.b
        q = self.q
        p = self.p
        rq = self.rq
        diu = self.diu
        diq = self.diq
        riu = self.riu
        riq = self.riq
        rid = self.rid
        xmu = self.xmu
        emu = self.emu 
        iumu = self.iumu
        idmu = self.idmu 
        iqmu = self.iqmu
        qv = self.qvol
        for i in range(total_nodes):
            prov = nodes[i]
            x = prov.sus 
            xq = prov.susQ
            iu = prov.iu
            i_d = prov.id 
            iq = prov.iq 
            e = prov.latent 
            eq = prov.latentQ
            rec = prov.rec
            death = prov.death
            lamb = prov.birth
            mu = prov.mu
            rmu = mu
            n0 = x + e + iu + i_d 
            death_nat = prov.death_nat
            for tau in range(100):
                x1 = ( lamb - mu * x  - (k*b/n0  + q*k*(1-b)/n0 )*iu*x - qv*x  + rq*xq) * 0.01 
                xq1 = ((q*k*(1-b)/n0)*iu*x + qv*x - rq*xq)*0.01 
                e1 = (-emu*e - p*e + (k*b*(1 - q))/n0*iu*x)*0.01 
                #e1 = (- p*e + (k*b*(1 - q))/n0*iu*x)*0.01 
                eq1 = ( (q*k*b/n0)*iu*x - p * eq)*0.01 
                iu1 = (p*e - (diu + riu + iumu)*iu)*0.01 
                id1 = (diu*iu + diq*iq - (rid + idmu)*i_d)*0.01 
                iq1 = (p*eq - (diq + riq + iqmu)*iq)*0.01 
                rec1 = (riu*iu + rid*i_d + riq*iq - rmu*rec)*0.01 
                #rec1 = (riu*iu + rid*i_d + riq*iq )*0.01 
                death1 = (iumu*iu + idmu*i_d + iqmu*iq)*0.01 
                death_nat1 = (mu * x + emu*e + rmu * rec)*0.01 
                # Update the variables
                x += x1
                xq += xq1 
                e += e1 
                eq += eq1
                iu += iu1
                i_d += id1 
                iq += iq1 
                rec += rec1 
                death += death1
                death_nat += death_nat1
                # if i == 0:
                #     #print(x + xq + e +eq + iu + i_d + iq + rec + death - x1 - xq1 - e1 - eq1 - iu1 - id1 - iq1 -rec1 -death1 )
                #     print(x1 + xq1 + e1 + eq1 + iu1 + id1 + iq1 + rec1 + death1 )
            # Update the state of the province
            prov.time = prov.time + 1 
            prov.iu = iu 
            prov.id = i_d 
            prov.iq = iq 
            prov.latent = e
            prov.latentQ = eq 
            prov.sus = x
            prov.susQ = xq 
            prov.death = death
            prov.rec = rec
            prov.death_nat = death_nat
            # We only count the live population
            prov.pop = x + xq + e + eq + iu + iq + i_d + rec
         



    def insert_infected(self, idx, number):
        # Method that insert a given number of 
        # infected people in a given idx province
        node = self.net_state.nodes[idx]
        node.iu = number


    def insert_latent(self, idx, number):
        # Method that insert a given number of 
        # latent people in a given idx province
        node = self.net_state.nodes[idx]
        node.latent = number
        node.pop += number


    def migration(self):
        # Method to move population between the provinces
        total_nod = self.net_state.N
        nodes = self.net_state.nodes
        # For all the nodes in the network
        for i in range(total_nod):
            # Define a dice 
            dice = random.random()
            # With probability migr 
            # the population of the i province
            # move to other province
            if dice <= nodes[i].migr:
                # For each neighbour of the province i 
                for neigh in nodes[i].cnx:
                    idx = neigh[0] # index of the province 
                    dist = neigh[1] # Distance between provinces
                    iu_a = nodes[i].iu * (1/(1 + dist)) * 0.001 # Infected people moved
                    e_a = nodes[i].latent * (1/(1 + dist)) * 0.001 # Latent people moved
                    x_a = nodes[i].sus * (1/(1 + dist)) * 0.001 # Susceptible people moved
                    rec_a = nodes[i].rec * (1/(1 + dist)) * 0.001 # Recovered people moved
                    # Update population node i
                    nodes[i].iu -=  iu_a
                    nodes[i].latent -=  e_a
                    nodes[i].sus -=  x_a
                    nodes[i].rec -= rec_a
                    nodes[i].pop -=  (x_a + iu_a + e_a + rec_a)
                    # Update population in the neighbour idx
                    nodes[idx].pop +=  x_a + iu_a + e_a  + rec_a
                    nodes[idx].iu += iu_a 
                    nodes[idx].latent += e_a 
                    nodes[idx].sus += x_a 
                    nodes[idx].rec += rec_a


    def get_inf(self, infec, t):
        nodes = self.net_state.nodes 
        N = self.net_state.N
        new_inf = infec
        for i in range(N):
            prov = nodes[i]
            aux = prov.iu + prov.id + prov.iq
            new_inf[i][t] = round(aux)
        return new_inf

    def get_inf_det(self, infec, t):
        nodes = self.net_state.nodes 
        N = self.net_state.N
        new_inf = infec
        for i in range(N):
            prov = nodes[i]
            aux = prov.id + prov.iq
            new_inf[i][t] = round(aux)
        return new_inf

    def get_inf_un(self, infec, t):
        nodes = self.net_state.nodes 
        N = self.net_state.N
        new_inf = infec
        for i in range(N):
            prov = nodes[i]
            aux = prov.iu 
            new_inf[i][t] = round(aux)
        return new_inf

    def get_inf_op(self, infec, t):
        nodes = self.net_state.nodes 
        N = self.net_state.N
        new_inf = infec
        for i in range(N):
            prov = nodes[i]
            n0 = prov.iu + prov.id + prov.iq + prov.latent + prov.latentQ + prov.sus + prov.susQ + prov.rec
            aux = prov.iu + prov.id + prov.iq
            new_inf[i][t] = aux/n0
        return new_inf

    def get_inf_det_op(self, infec, t):
        nodes = self.net_state.nodes 
        N = self.net_state.N
        new_inf = infec
        for i in range(N):
            prov = nodes[i]
            n0 = prov.iu + prov.id + prov.iq + prov.latent + prov.latentQ + prov.sus + prov.susQ + prov.rec
            aux = prov.id + prov.iq
            new_inf[i][t] = aux/n0
        return new_inf

    def get_inf_un_op(self, infec, t):
        nodes = self.net_state.nodes 
        N = self.net_state.N
        new_inf = infec
        for i in range(N):
            prov = nodes[i]
            n0 = prov.iu + prov.id + prov.iq + prov.latent + prov.latentQ + prov.sus + prov.susQ + prov.rec
            aux = prov.iu 
            new_inf[i][t] = aux/n0
        return new_inf
        
    def get_death_op(self, infec, t):
        nodes = self.net_state.nodes 
        N = self.net_state.N
        new_inf = infec
        for i in range(N):
            prov = nodes[i]
            n0 = prov.iu + prov.id + prov.iq + prov.latent + prov.latentQ + prov.sus + prov.susQ + prov.rec
            aux = prov.death 
            new_inf[i][t] = aux/n0
        return new_inf

    def get_death(self, infec, t):
        nodes = self.net_state.nodes 
        N = self.net_state.N
        new_inf = infec
        for i in range(N):
            prov = nodes[i]
            aux = prov.death 
            new_inf[i][t] = round(aux)
        return new_inf

    def print_data(self, data, file_name):
        file_dat = open(file_name, "w")
        N = len(data)
        line = len(data[0])
        for i in range(N):
            for j in range(line):
                file_dat.write(str(data[i][j]))
                file_dat.write("\t")
            file_dat.write("\n")
        file_dat.close()


    def matrix_mult(self, mat, num):
        n = len(mat)
        m = len(mat[0])
        new_mat = [ [ 0 for i in range(m) ] for j in range(n) ]
        for i in range(n):
            for j in range(m):
                new_mat[i][j] = mat[i][j]*num
        return new_mat
        

    def simulation(self, file_name):
        # Method that run a complet simulation of 
        # the coronavid19 in a given network

        T_total = self.T
        N = self.net_state.N
        infectious = [ [ 0 for i in range(T_total) ] for j in range(N) ] 
        inf_unde = [ [ 0 for i in range(T_total) ] for j in range(N) ] 
        inf_det = [ [ 0 for i in range(T_total) ] for j in range(N) ] 
        mu = [ [ 0 for i in range(T_total) ] for j in range(N) ] 

        # op_inf = [ [ 0 for i in range(T_total) ] for j in range(N) ] 
        # op_inf_unde = [ [ 0 for i in range(T_total) ] for j in range(N) ] 
        # op_inf_det = [ [ 0 for i in range(T_total) ] for j in range(N) ] 
        # op_mu = [ [ 0 for i in range(T_total) ] for j in range(N) ] 

        for t in range(T_total):
            self.dynamic_step()
            # op_inf = self.get_inf_op(op_inf, t)
            # op_inf_unde = self.get_inf_un_op(op_inf_unde, t)
            # op_inf_det = self.get_inf_det_op(op_inf_det, t)
            mu = self.get_death(mu, t)

            infectious = self.get_inf(infectious, t)
            inf_unde = self.get_inf_un(inf_unde, t)
            inf_det = self.get_inf_det(inf_det, t)
#            op_mu = self.get_death_op(mu, t)
            
            if t <= 13:     
                self.migration()
            # self.save_color_graph(file_name+str(t))
            self.print_states(file_name+str(t))
            #print("time: {} Param  : {} \n".format(t, self.net_state.nodes[1].vec_Param))
        max_inf = max(flatten(infectious))
        # max_inf_unde = max(flatten(inf_unde))
        # max_inf_det = max(flatten(inf_det))
        # max_mu = max(flatten(mu))
        
        norm_inf = self.matrix_mult(infectious, (1/max_inf))
        norm_inf_unde = self.matrix_mult(inf_unde, (1/max_inf))
        norm_det =self.matrix_mult(inf_det, (1/max_inf))
        norm_mu = self.matrix_mult(mu, (1/max_inf))
        self.print_data(infectious,"infected.dat")
        self.print_data(inf_det,"infected_detected.dat")
        self.print_data(inf_unde,"infected_undetected.dat")
        self.print_data(mu,"death.dat")
        self.print_data(norm_inf,"opacity_inf.dat")
        self.print_data(norm_det,"opacity_inf_det.dat")
        self.print_data(norm_inf_unde,"opacity_inf_un.dat")
        self.print_data(norm_mu,"opacity_death.dat")
        # self.print_data(op_inf,"opacity_inf.dat")
        # self.print_data(op_inf_det,"opacity_inf_det.dat")
        # self.print_data(op_inf_unde,"opacity_inf_un.dat")
        # self.print_data(op_mu,"opacity_death.dat")


    def coloring_val(self, graph):
        base = self.Q
        length = self.F
        nodes = self.net_state.nodes
        step = 1/(base**length)
        val_map = lambda i:  step*i 
        values = [val_map(self.n_base_transf(nodes[node])) for node in graph.nodes()]
        return values

     
    def plot_color_graph(self):
        # Method that plot the network. It return an
        # image of the topology of the network.
        N = self.net_state.N
        positions = self.net_state.positions
        edges = []
        for i in range(N):
            cnx = self.net_state.nodes[i].cnx
            for j in cnx: 
                edges.append([i,j])
        gr = nx.Graph() 
        # Initialize the graph
        dic_prov = list_provinces() # List with province and index ("prov", idx)
        labels = [ x[0] for x in dic_prov ]
        gr.add_edges_from(edges)
        # Add the edges to graph
        #colors = self.coloring_val(gr)
        nx.draw_networkx(gr, pos=positions,  labels= labels, with_labels=True, node_size=250, font_color='black')
        # Define the characteristics of the plot
        #plt.savefig(file_name)
        plt.show()   

    def save_color_graph(self, file):
        # Method that plot the network. It return an
        # image of the topology of the network.
        N = self.net_state.N
        positions = self.net_state.positions
        edges = []
        for i in range(N):
            cnx = self.net_state.nodes[i].cnx
            for j in cnx: 
                edges.append([i,j[0]])
        gr = nx.Graph() 
        gr.add_edges_from(edges)
        # List with province and index ("prov", idx)
        dic_prov = list_provinces() 
        labels = [ x[0] for x in dic_prov ]
        # Initialize the graph
        for i in range(len(positions)):
             gr.add_node(i, pos= positions[i])
        lab = {}
        for j in range(len(labels)):
            lab[j] = labels[j]

        pos=nx.get_node_attributes(gr,'pos')
        nx.draw_networkx(gr, pos= pos, arrows=True, with_labels=False, node_size=200, font_color='black')
        nx.draw_networkx_labels(gr, pos, lab)
        # Define the characteristics of the plot
        #plt.savefig(file_name)
        #plt.show() 
        plt.savefig(file)
        plt.close()
        #plt.show()       
            
    def dictionary_prov(self):
        file_prov = open("provincias.dat","r")
        dictionary = []
        for line in file_prov:
            aux = line.split(" ")
            aux[1] = aux[1][:-1]
            dictionary.append(aux[1])
        return dictionary

    def print_states(self, fileName):
        dataFile = open(str(fileName)+".dat","w")
        totalN = self.net_state.N
        prov_name = self.dictionary_prov()
        nodes = self.net_state.nodes
        for i in range(totalN):
            dataFile.write("Province: "+prov_name[i]+"\tPop :"+str(round(nodes[i].pop))+"\nInfected :"+str( round(nodes[i].iu + nodes[i].id + nodes[i].iq))+"\nInfected Undetected :"+str(round(nodes[i].iu))+"\nSusceptible :"+str(round(nodes[i].sus) )+"\nSusceptible Quarantined :"+str(round(nodes[i].susQ))+"\nDeath :"+str(round(nodes[i].death))+"\nRecovered :"+str(round(nodes[i].rec))+"\nNatural Deaths :"+str(round(nodes[i].death_nat) ) )
            dataFile.write("\n")
            dataFile.write("-----------------------------------------------------------------------------\n")
        dataFile.close()

    def print_province(self, idx):
        i = idx
        nodes = self.net_state.nodes
        prov_name = self.dictionary_prov()
        print("Province: "+prov_name[i]+"\tPop :"+str(nodes[i].pop)+"\nInfected :"+str(nodes[i].iu + nodes[i].id + nodes[i].iq)+"\n Infected Undetected"+str(nodes[i].iu)+"\nSusceptible :"+str(nodes[i].sus )+"\nSusceptible Quarantined :"+str(nodes[i].susQ)+"\nDeath :"+str(nodes[i].death)+"\nRecovered :"+str(nodes[i].rec) )

def list_provinces():
    prov_file = open("provincias.dat","r")
    dic_prov = []
    for line in prov_file:
        aux = line.split("   ")
        aux[0] = int(aux[0])
        aux[1] = aux[1][:-1]
        dic_prov.append( (aux[1], aux[0]) )
    return dic_prov

def ord_provinces(file_name):
    dic_prov = list_provinces() # Obtain the dictionary of provinces
    n = len(dic_prov) # len of the dic
    doc = open(file_name, "r") # open the file to orders
    ord_list = [0]*n 
    for line in doc:
        aux = line.split("\t")
        dat = float(aux[1][:-1])
        idx = [ x for x in dic_prov if x[0] == aux[0] ][0][1]
        ord_list[idx] = dat
    return ord_list

        

flatten = lambda l: [item for sublist in l for item in sublist]
 

       