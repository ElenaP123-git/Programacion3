matriz = [[1,2,3],[0,2,2],[4,4,2]]
def suma_fila(matriz, numfila):
    total = 0
    fila = matriz[numfila]
    for elemento in fila:
        total = total + elemento
    return total
sumafila = suma_fila(matriz, 1) # suma la segunda fila
print(sumafila)