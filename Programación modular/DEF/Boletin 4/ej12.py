def crear_matriz_posicion(num_filas, num_columnas):
    matriz = [] 

    for i in range(num_filas):
        fila = []  
        
        for j in range(num_columnas):
            valor = i + j
            fila.append(valor)
        matriz.append(fila)
        
    return matriz

filas = 2
columnas = 5

matriz_generada = crear_matriz_posicion(filas, columnas)

for fila in matriz_generada:
    print(fila)
