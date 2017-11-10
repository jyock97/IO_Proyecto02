# Comparación entre Programación Dinámica y Fuerza Bruta

### Problema de la Mina

El problema de la mina puede resolverse de manera dinamica utilizando una matriz para guardar los resultados anteriores en el proceso.

La complegidad temporal resolviendo el problema por fuerza bruta es de O(n*3^n).

La complegidad temporal resolviendo el problema utilizando programacion dinámica es O(n*n*m) = O(n^2*m)

Al comparar ambos algoritmos, se nota una gran diferencia entre mayor sea el tamaño de la matriz, especial mente cuanto más cresca m, más va a tardar el algoritmo de fuerza bruta en terminar.

![Ejemplo con matriz 3x3](./resultadoMina2.png)

![Ejemplo con matriz 3x12](./resultadoMina1.png)


### Problema Mochila
