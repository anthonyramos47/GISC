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
medias_ar = [(0.25, 0.25), (0.1, 0.5)]
# Datos a correr por Oscar
# medias_oscar = [(0.33,0.33), (0.1, 0,8), (0.02, 0.02)]

# Datos Anthony
f = open("Data_SN_"+str(medias_ar[rank][0])+"_"+str(medias_ar[rank][1])+".dat","w")
# Datos Oscar
# f = open("Data_SN_"+str(medias_oscar[rank][0])+"_"+str(medias_oscar[rank][1])+".dat","w")

for i in range( 1 , 1001, 10 ):
     F = 10 # Longitud de los vectores de opinion
     Q = 1 - (1 - 1/i)**F # Valor modificado de q solo para plot
     averageS1 = 0 # Porcion Promedio de la poblacion mas grande
     averageS2 = 0 # Porcion Promedio de la segunda poblacion mas grande
     for j in range(5):
          # Inicializamos la dinamica
          dyn = TwoMedia(graph=SN, tot_par = F, tot_opt = i, B=medias_ar[rank][0], B2=medias_ar[rank][1], n_ch=1, T=200)
          # Inicializamos la toma de datos
          dic = dyn.get_data()
          averageS1 +=dic[0][1]/800
          averageS2 +=dic[1][1]/800 
     # Sacamos un promedio de los datos tomados
     averageS1 /= 5
     averageS2 /= 5
     # Cadena a escribir en el archivo
     cad = str(Q)+" "+str(averageS1)+" "+str(averageS2)+"\n"

     f.write(cad)
f.close
   
