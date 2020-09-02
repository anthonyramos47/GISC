from topologies import SmallWorldNetwork, CompleteNetwork, SquareNetwork, ScaleFreeNetwork
from dynamics import TwoMedia, Homophily
import time
from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD # Communicador de MPI 
size = comm.Get_size() # Numero total de Procesadores
rank = comm.Get_rank() # Id de cada procesador

# Topologia de la red
SN = SquareNetwork(height = 40, width  = 40)

# Tipos de datos por media [(B,B2)]
# Datos a correr por Anthony
medias = [(0.25, 0.25), (0.1, 0.5), (0.1, 0.8)]
# Datos a correr por Oscar
# medias_ar = [(0.1, 0.8)]

# Datos Anthony
f = open("Data_SN_"+str(medias[rank][0])+"_"+str(medias[rank][1])+".dat","w")
# Datos Oscar
# f = open("Data_SN_"+str(medias_oscar[rank][0])+"_"+str(medias_oscar[rank][1])+".dat","w")
step = 0.009
for i in range( 1 , 100):
     F = 10 # Longitud de los vectores de opinion
     Q = step*i # Valor Q
     q = int(-(1/(-1 + (1 - Q)**(1/F)))) # Obtenemos q a partir de Q
     averageS1 = 0 # Average of the main majority
     averageS2 = 0 # Average of the second majority
     averageB = 0  # Average Population with the same opinion as B
     averageB2 = 0 # Average Population with the same opinion as B2
     for j in range(5):
          # Inicializamos la dinamica
          dyn = TwoMedia(graph=SN, tot_par = F, tot_opt = q, B=medias[rank][0], B2=medias[rank][1], n_ch=1, T=200)
          # Inicializamos la toma de datos
          dic = dyn.get_data()
          averageS1 += dic[0]/1600
          averageS2 += dic[1]/1600 
          averageB  += dic[2]/1600
          averageB2 += dic[3]/1600
     # Sacamos un promedio de los datos tomados
     averageS1 /= 5
     averageS2 /= 5
     # Cadena a escribir en el archivo
     cad = str(Q)+" "+str(averageS1)+" "+str(averageS2)+"\n"

     f.write(cad)
f.close
   
