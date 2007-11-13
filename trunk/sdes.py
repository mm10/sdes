from claves import * #generacion de claves
import operator

def ip(ent):
    """permutacion de bits IP
    2 6 3 1 4 8 5 7
    """
    sal = []
    for i in  [2, 6, 3, 1, 4, 8, 5, 7]:
       sal.append(ent[i-1])
    print "........IP: " + str(sal)   
    return sal

def ip_1(ent):
    """" permutacion de bits IP-1
      IP-1
    4 1 3 5 7 2 8 6"""
    sal = []
    for i in  [4, 1, 3, 5, 7, 2, 8, 6]:
       sal.append(ent[i-1])
    print "........IP-1: " + str(sal)   
    return sal

def ep(ent):
    """permutacion de expansion
          E/P
    4 1 2 3 2 3 4 1
    """    
    sal = []
    for i in [4, 1, 2, 3, 2, 3, 4, 1]:
        sal.append(ent[i-1])
    print "........E/P: " + str(sal)           
    return sal

def xor(var1, var2):
    assert(len(var1)==len(var2))
    sal = [operator.xor(var1[i],var2[i]) for i in range(len(var1))]
    print "........xor: " + str(sal) 
    return sal
    
def s(ent,tipo):
    """   
    S0 | 00 01 10 11
    -----------------
    00 | 01 00 11 10
    01 | 11 10 01 00
    10 | 00 10 01 11
    11 | 11 01 11 10

    S1 | 00 01 10 11
    -----------------
    00 | 00 01 10 11
    01 | 10 00 01 11
    10 | 11 00 01 00
    11 | 10 01 00 11

    El renglon lo conforman el primero y el cuarto bit. La columna el 2 y el 3. 
    """
    assert(len(ent)==4)
    assert(tipo==0 or tipo==1)
    
    if [ent[0],ent[3]]==[0,0]:
        if [ent[1],ent[2]] == [0,0]:
            s = [0,1],[0,0] 
        if [ent[1],ent[2]] == [0,1]:
            s = [0,0],[0,1]
        if [ent[1],ent[2]] == [1,0]:
            s = [1,1],[1,0]
        if [ent[1],ent[2]] == [1,1]:
            s = [1,0],[1,1]

    if [ent[0],ent[3]]==[0,1]:
        if [ent[1],ent[2]] == [0,0]:
            s = [1,1],[1,0]
        if [ent[1],ent[2]] == [0,1]:
            s = [1,0],[0,0]
        if [ent[1],ent[2]] == [1,0]:
            s = [0,1],[0,1]
        if [ent[1],ent[2]] == [1,1]:
            s = [0,0],[1,1]

    if [ent[0],ent[3]]==[1,0]:
        if [ent[1],ent[2]] == [0,0]:
            s = [0,0],[1,1]
        if [ent[1],ent[2]] == [0,1]:
            s = [1,0],[0,0]
        if [ent[1],ent[2]] == [1,0]:
            s = [0,1],[0,1]
        if [ent[1],ent[2]] == [1,1]:
            s = [1,1],[0,0]        

    if [ent[0],ent[3]]==[1,1]:
        if [ent[1],ent[2]] == [0,0]:
            s = [1,1],[1,0]
        if [ent[1],ent[2]] == [0,1]:
            s = [0,1],[0,1]
        if [ent[1],ent[2]] == [1,0]:
            s = [1,1],[0,0]
        if [ent[1],ent[2]] == [1,1]:
            s = [1,0],[1,1]
    print "........S" + str(tipo) + ": " + str(s[tipo])
    return s[tipo]  #S0


def p4(ent):
    """permutacion de bits P4
    2 4 3 1
    """
    sal = []
    for i in  [2, 4, 3, 1]:
       sal.append(ent[i-1])
    print "........P4: " + str(sal)   
    return sal

def sw(ent):
    """invierte el orden de los nibbles"""
    return ent[4:] + ent[:4]

    
def fk(ent, k):
    print "======================== Inicio de FK ============================="
    L = ent[:4]
    R = ent[4:]
    print "........L: " + str(L) + "........R: " + str(R) 
    parcial = ep(R) #expansion EP
    parcial = xor(parcial,k) #exorea con la salida de EP con k
    parcial = s(parcial[:4],0) + s(parcial[4:],1) #aplico las cajas s0 y s1 y concateno los resultados. 
    parcial = p4(parcial) #aplica permutacion p4
    parcial = xor(L, parcial) #exorea con L
    print "........Fk: " + str(parcial + R)
    return parcial + R
    
 
 
def sdes(M,K):
    """algoritmo principal"""
    k1,k2 = claves(K) #genero las claves
    sdes = ip(M) 
    sdes = fk(sdes,k1) #primera ronda
    sdes = sw(sdes)
    sdes = fk(sdes,k2) #segunda ronda
    sdes = ip_1(sdes)
    #print "M = %s\nK = %s\nC = %s" % str(M),str(K),str(sdes)
    return sdes
    
       
if __name__ == '__main__':
	M = [1,0,1,1,1,1,0,1]
	K = [1,0,1,0,0,0,0,0,1,0]
	#K = ['k1','k2','k3','k4','k5','k6','k7','k8','k9','k10']
	print "Caracter codificado: " +  str(sdes(M,K))


 
 
