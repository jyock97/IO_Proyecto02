
import random
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

def main():
    generadorMinas("prueba.txt",4,8)

main()
