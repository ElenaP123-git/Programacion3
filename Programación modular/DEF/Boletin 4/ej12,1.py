filas = 4
columna = 5

def genera_matriz(filas,columnas):
    matriz = []
    for i in range (filas):
        fila = []
        for columna in range(columnas):
            fila.append(i + columna)
        matriz.append(fila)
    return matriz

matriz_completa = genera_matriz(filas, columna)
print(matriz_completa)
