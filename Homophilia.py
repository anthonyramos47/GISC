def homophile(net,n_ach):
    N=net.N
    for i in range(N):
        n1=i
        n2=random.choice(net.nodes[n1].cnx)
        vec_sim=Sim(net,n1,n2)      #Obtener vector booleano. 1 equal. 0 diff.
        P=np.sum(vec_sim)/net.nodes[n1].F   #probabilidad de interactuar
        if(random.random()<P):
            atrs_ch=select_atr(vec_sim,n_ach)  #Obtener lista de indices de atributos a cambiar
            for atr in atrs:
                net.nodes[n1].vec_Param[atr]=net.nodes[n2].vec_Param[atr]

def Sim(net,n1,n2):
    F=net.nodes[n1].F
    vec_s=[]
    candidates=[]
    atrs_ch=[]
    
    for i in range F:
        if net.node[n1]==net.node[n2]:
            vec_s[i]=1
        else:
            vec_s[i]=0
    return vec_s

def select_atr(vec_sim, n_ach):
    
    not_eq=F-np.sum(vec_sim)
    if n_ach > not_eq:
        n_ach=not_eq
    
    candidates=[]
    
    for i in range(len(vec_sim)):
        if vec_sim[i]==0:
            candidates.append(i)
    
    for i in range n_ach:
        selec=random.choice(candidates)
        atrs_ch.append(selec)
        candidates.remove(selec)
        
    return atrs_ch
        