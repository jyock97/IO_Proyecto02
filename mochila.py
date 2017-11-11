import time
import argparse
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
    parser = argparse.ArgumentParser(description="Programa para calcular el problema de la mochila")
    parser.add_argument("input", help="Archivo de entrada para el programa")
    parser.add_argument("-o","--output", help="Archivo de salida para el programa", default="resultKnapsack.jpg")
    args = parser.parse_args()
    inputFile = args.input
    outputFile = args.output

    with open(inputFile) as f:
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


    initialtime = time.time()#toma el tiempo al inicio
    dintime = 0
    emptymemo = memo#guarda el memoize vacio
    #10 corridas con dinamica
    for i in range(10):#corre 10 veces el algoritmo
        solve(0,0,capacity,True)
        memo = emptymemo#reinicia el memoize
    auxtime = time.time()#toma el tiempo que duro las 10 corridas
    dintime += (auxtime-initialtime)#suma la diferencia

    backtime = 0
    #diez corridas con fuerza bruta
    for i in range(9):#corre 10 veces la prueba
        solve(0,0,capacity,False)
    backtime += (time.time()-auxtime)#corre 9 veces
    print(solve(0,0,capacity,False))
    backtime += (time.time()-auxtime)#la decima vez que corre imprime el resultado

    draw(dintime/10, backtime/10, outputFile)
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

#Metodo que dibuja los resultados obtenidos
def draw(dp, force, outputFile):
    method = ("Dinamica", "Fuerza Bruta")
    posicion_x = np.arange(2)
    plt.bar(posicion_x, [dp,force], color = "g")
    plt.ylabel('Tiempo en Segundos')
    plt.xticks(posicion_x+0.4,['Dinamica',' Fuerza Bruta'])
    plt.title("Comparacion de metodos")
    plt.savefig(outputFile)



if __name__ == '__main__':
    main()
