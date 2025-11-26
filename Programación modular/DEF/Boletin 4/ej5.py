# suma numeros pares de la matriz
matriz = [[2,3,4],[2,2,4],[0,1,3]]

def calc_num_pares(matriz):
    lista_pares = []
    for i in range(len(matriz)):
        fila = matriz[i]
        for e in fila:
            if e % 2 == 0:
                lista_pares.append(e)
    return lista_pares

def suma_fila(lista_pares):
    suma = 0
    for i in lista_pares:
        suma = i + suma
    return suma

pares = calc_num_pares(matriz)
print(pares)
suma_pares = suma_fila(pares)
print(suma_pares)