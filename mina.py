import sys
import argparse
import time
import matplotlib.pyplot as plt
import numpy as np

mat = []
res = []
n = 0
m = 0

def draw(timeDp, timeBf, outputFile):
    method = ("Dinamica", "Fuerza Bruta")
    posicion_x = np.arange(2)
    plt.bar(posicion_x, [timeDp,timeBf], color = "b")
    plt.ylabel('Tiempo en Segundos')
    plt.xticks(posicion_x+0.4,['Dinamica',' Fuerza Bruta'])
    plt.title("Comparacion de metodos")
    plt.savefig(outputFile)
    
def solve(i, j, bDinamica):
    global mat, res, n, m

    if (i < 0 or i >= n):
        return -1

    if (j == m-1):
        res[i][j] = mat[i][j]
        return res[i][j]

    if(bDinamica):
        if(res[i][j] != 0):
            return res[i][j]

    res[i][j] = mat[i][j] + max(solve(i-1, j+1, bDinamica),
                                solve(i, j+1, bDinamica),
                                solve(i+1, j+1, bDinamica))
    return res[i][j]

def main():
    global mat, res, n, m
    maxNum = 0

    parser = argparse.ArgumentParser(description="Programa para calcular el problema de la mina")
    parser.add_argument("input", help="Archivo de entrada para el programa")
    parser.add_argument("-o","--output", help="Archivo de salida para el programa", default="resultMine.pdf")
    args = parser.parse_args()
    inputFile = args.input
    outputFile = args.output

    with open(inputFile) as f:

        i = 0
        for line in f:
            line = line.rstrip("\n")
            mat.append([])
            res.append([])
            for num in line.split(", "):
                mat[i].append(int(num))
                res[i].append(0)
            i+=1

    n = len(mat)
    m = len(mat[0])

    #Correr la solucion con programacion dinamica
    startTime = time.time()
    for i in range(0, n):
        maxNum = max(maxNum, solve(i, 0, True))
    endTime = time.time()
    timeDp = endTime - startTime
    print("Tiempo en resolver con Programacion Dinamica: " + str(timeDp))

    #Limpiar la matriz de resultado para utilizarla de nuevo
    for i in range(0, len(res)):
        for j in range(0, len(res[i])):
            res[i][j] = 0

    #Correr la solucion con fuerza bruta
    startTime = time.time()
    for i in range(0, n):
        maxNum = max(maxNum, solve(i, 0, False))
    endTime = time.time()
    timeBf = endTime - startTime
    print("Tiempo en resolver con Fuerza Bruta: " + str(timeBf))

    draw(timeDp, timeBf, outputFile)
    print("Resultado: " + str(maxNum))

if __name__ == '__main__':
    main()
