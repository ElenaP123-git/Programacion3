# matriz cuadrada (fila = columna)
matriz = [[8, 1, 6],
          [3, 5, 7],
          [4, 9, 2]]

def es_cuadrada(matriz):
    num_filas = len(matriz) # (3 filas)
    num_columnas = len(matriz[0]) # len(primera fila) = (3) --> para que sea tres también la primera columna
    return num_filas == num_columnas # devuelve la función si las columnas = filas

def devuelveDiagonal(matriz):
    fila = 0
    col = 0
    lista = []
    if es_cuadrada(matriz):
        for i in range(len(matriz)):
            lista.append(matriz[fila][col])
            fila += 1
            col += 1
    return lista

print(devuelveDiagonal(matriz))


def otraDiagonal(matriz):
    fila = 0
    col = len(matriz) - 1 # empieza desde el último elemento de la última fila
    lista = []
    if es_cuadrada(matriz):
        for i in range(len(matriz)):
            lista.append(matriz[fila][col]) 
            fila += 1
            col -= 1 
    return lista

print(otraDiagonal(matriz))

