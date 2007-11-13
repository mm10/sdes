def p10(ent):
    """permutacion de bits P10
    3 5 2 7 4 10 1 9 8 6
    """
    sal = []
    for i in  [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]:
       sal.append(ent[i-1]) 
    print "........p10: " + str(sal)   
    return sal

def p8(ent):
    """permutacion de bits  P8
    6 3 7 4 8 5 10 9
    """
    sal = []
    for i in  [6, 3, 7, 4, 8, 5, 10, 9]:
       sal.append(ent[i-1])
    print "........p8: " + str(sal)          
    return sal
           
def shift(ent, cant=1):
    """separa en 2 nibbles, les rota cant bit(s) a izquierda a cada 1, y los devuelve"""
    bajo = ent[:5]
    alto = ent[5:]
    print "........bajo: " + str(bajo) + "........alto: " + str(alto) 
    print "........" + str(cant) + " rotaciones a izquierda"
    for i in range(cant):
        bajo.insert(5,bajo.pop(0))  #rotacion a la izquierda
        alto.insert(5,alto.pop(0))
        #bajo.insert(0,bajo.pop())
        #alto.insert(0,alto.pop())
    print "........shift: " + str(bajo + alto)
    return bajo + alto
    
def claves(K):
    print "======================== Generacion de clave ============================="
    print "K = " + str(K)
    k1 = p8(shift(p10(K)))
    k2 =  p8(shift(p10(K),3))
    print "K1 = " + str(k1)
    print "K2 = " + str(k2)
    return k1,k2


        
