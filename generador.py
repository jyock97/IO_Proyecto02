
import random
# Funcion que genera la matriz para la mina que resive como parametros:
# nombre, que es el nombre del arcivo en el que se va a escribir la matriz
# n, que es la cantidad de filas
# m, la cantidad de columnas
def generadorMinas (nombre,n, m):
    archivo = open(nombre, "a")
    for i in range(n):
        if i != 0:
            archivo.write("\n")
        for j in range(m):
            archivo.write(str(random.randint(0,100)))
            if j != m-1:
                archivo.write(", ")
    archivo.close()

# Funcion que genera el peso y los dos arreglos para el problema de mochila que resive como parametros:
# nombre, que es el nombre del arcivo en el que se van a escribir los valores
# n, que es el tamano de la mochila (tamano de los arreglos)
def generadorMochila (nombre,n):
    archivo = open(nombre, "a")
    archivo.write(str(random.randint(30,97)))#este es el peso de la meochila
    archivo.write("\n")
    for i in range(n):
        archivo.write(str(random.randint(1,60)))#estos son los pesos de cada elemento
        if i != n-1:
            archivo.write(", ")
    archivo.write("\n")
    for j in range(n):
        archivo.write(str(random.randint(20,100)))#estos son los beneficios de cada elemento
        if j != n-1:
            archivo.write(", ")
    archivo.close()

def main():
    generadorMinas("prueba.txt",4,8)
    generadorMochila("prueba2.txt",8)

main()

