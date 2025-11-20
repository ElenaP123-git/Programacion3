def estaOrdenada(lista): # coge la lista de abajo
    ordenada = True
    i = 0
    while i < len(lista)-1 and ordenada:
        if lista[i] > lista [i + 1]:
            ordenada = False
        i +=1
    return ordenada

lista = [1,2,3,4]
orden = estaOrdenada(lista) # orden = estaOrdenada([1,2,3,4])
print(orden)

lista = [1,8,3,4]
orden = estaOrdenada([1,8,3,4]) # orden = estaOrdenada([1,8,3,4])
print(orden)