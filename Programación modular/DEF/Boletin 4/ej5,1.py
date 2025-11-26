# suma filas pares
matriz = [[8,1,6],[3,5,7],[4,9,2]]

def suma_fila_pares(matriz):
    suma = 0
    for numfila in range (len(matriz)):
        if numfila% 2 == 0:
            for elemento_fila in matriz[numfila]:
                suma = suma + elemento_fila
    return suma
print("La suma de los números de las filas pares es:",suma_fila_pares(matriz))