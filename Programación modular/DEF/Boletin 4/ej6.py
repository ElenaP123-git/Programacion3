#suma elementos de una columna
def suma_columna(matriz,num_columna):
    suma = 0
    columna = calc_lista_columna(num_columna,matriz)
    for i in columna:
        suma = suma + i
        return suma

def calc_lista_columna(columna, matriz):
    lista_columna = []
    for fila in range (len(matriz)):
        lista_columna.append(matriz[fila][columna])
    return lista_columna

matriz = [[8,1,6],[3,5,7],[2,9,2]]
print(suma_columna(matriz,0))
