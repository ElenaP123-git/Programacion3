lista = [1,2,3,4,5]
matriz = [[1,2,3],[0,4,5],[2,2,3]]

def suma(lista):
    pareslist = []
    for i in lista:
        if i % 2 == 0:
            pareslist.append(i)
    return pareslist 

def paresMatriz(matriz):
    pares = []
    for i in matriz:
        for z in i:
            if z % 2 == 0:
                pares.append(z)
    return pares 

sumita = suma(lista)
prs = paresMatriz(matriz)
print(sumita)
print(prs)