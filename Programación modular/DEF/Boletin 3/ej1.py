def obtengolista(): #lee lista por teclado
    lista = []
    rep = True
    while rep:
        num = int(input("Introduce un número: "))
        lista.append(num)
        if num == 0:
            rep = False
    #todo
    return lista

def listainvertida(lista): # a partir de una lista devolver la lista invertida
    print(lista)
    invertida = []
    for i in range (len(lista)-1,-1,-1):
        invertida.append(lista[i])
    #todo
    return invertida

listainicial = obtengolista(1, 2)
listainversa = listainvertida(listainicial)
print(listainversa)