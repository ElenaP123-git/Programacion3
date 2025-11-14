def estaOrdenada(lista): # coge la lista de abajo
    ordenada = True
    i = 0
    while i < len(lista)-1:
        if lista[i] > lista [i + 1]:
            ordenada = False
        i +=1
    return ordenada

# Pruebas
print(estaOrdenada([1, 2, 3, 4]))   
print(estaOrdenada([1, 8, 3, 4]))   
print(estaOrdenada([10, 20, 20]))  
print(estaOrdenada([]))        
print(estaOrdenada([7]))       
