from topologies import SmallWorldNetwork, CompleteNetwork, SquareNetwork, ScaleFreeNetwork
from dynamics import TwoMedia, Homophily
import time



SN = SquareNetwork(height = 40, width  = 40)
dyn = TwoMedia(graph=SN, tot_par=10, tot_opt= 10000, B=0.5, R=0.3, n_ch= 1, tol=10)
dyn.data_sim()
# f = open("prueba.dat","w")
# t = time.time()     
# for i in range(1,150):
#      F = 10
#      Q = 1 - (1 - 1/i)**F
#      averageS1 = 0
#      averageS2 = 0
#      for j in range(5):
#           dyn = TwoMedia(graph=SN, tot_par = F, tot_opt = i, B=0.02, B2=0.5, n_ch=1, T=10)
#           dic = dyn.get_data()
#           averageS1 +=dic[0][1]/800 
#           averageS2 +=dic[1][1]/800 
#      averageS1 /= 5
#      averageS2 /= 5
#      cad = str(Q)+" "+str(averageS1)+" "+str(averageS2)+"\n"
#      f.write(cad)
# t_end = time.time()
# print("Tiempo:",(t_end-t))
# f.close
   
# Q [0, 1]
# [0 0 1 0]  F = 4  q = 10000

#CN = CompleteNetwork(N = 4)
#CN.draw_network()
#f = open("sq_net_time.dat","w")
#for n in range(2,500):
#     t_g = time.time()

#      t_end = time.time()
#      f.write(str(n)+" "+str(t_end - t_g)+"\n")
# f.close()
#SN.draw_network()

#SFN = ScaleFreeNetwork(100)
#SFN.draw_network()

#SWN = SmallWorldNetwork(N = 50,K = 5,p = 1)
#SWN.draw_network(with_labels = True)