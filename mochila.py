import time
import matplotlib.pyplot as plt
import numpy as np
#valores globales de la mochila de entrada
capacity = 0
weight = []
value = []
memo = []
#funcion que resuelve mochila
#Si mode es true, utiliza el memoize por lo que es dinamica
#si es falso entonces no recuerda los valores y hace el metodo backtracking
def solve(item, val, cap, mode):
    global weight, value, memo
    if(item < len(weight) and cap>=0 and memo[cap][item]>0 and mode):
        return memo[cap][item]
    if(cap<0):
        return 0
    if(item>=len(weight)):
        return val
    memo[cap][item] = max(solve(item+1,val+value[item],cap-weight[item],mode),solve(item+1,val,cap,mode))
    return memo[cap][item]

def main():
    global capacity,memo
    with open("mochila.txt") as f:
        i = 0
        for line in f:
            if(i == 0):
                capacity = int(line)
            else:
                temp = line.rstrip("\n")
                for num in temp.split(","):
                    if(i == 1):
                        weight.append(int(num))
                    else:
                        value.append(int(num))
            i+=1
    for i in range(capacity+1):
        memo.append([])
        for j in range(len(weight)):
            memo[i].append([])
            memo[i][j] = 0
    initialtime = time.time()
    solve(0,0,capacity,True)
    auxtime = time.time()
    dintime = auxtime-initialtime
    print(solve(0,0,capacity,False))
    backtime = time.time()-auxtime
    draw(dintime, backtime)
    aux = 0
    items = []
    for i in range(1,len(weight)):
        if(memo[-1][aux]!=memo[-1][i] and capacity>0):
            items.append(i)
            capacity-=weight[aux]
            aux = i
    if(capacity>0 and weight[-1]<capacity):
        items.append(len(weight))
    print(items)

def draw(dp, force):
    method = ("Dinamica", "Fuerza Bruta")
    posicion_x = np.arange(1)
    unidades = (dp, force)
    plt.bar(posicion_x+0, [dp], color = "b", width = 0.25)
    plt.bar(posicion_x+0.75, [force], color = "g", width = 0.25)
    plt.xticks(posicion_x+0, ["Dinamica","Fuerza Bruta"])
    
    plt.ylabel('Tiempo en Segundos')
    plt.title("Comparacion de metodos")
    plt.savefig("Hola.pdf")



if __name__ == '__main__':
    main()
