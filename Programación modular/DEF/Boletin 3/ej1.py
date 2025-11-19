def obtengolista():  # lee lista por teclado
    lista = []
    # todo
    while True:
        num = int(input("Introduce un número (0 para terminar): "))
        lista.append(num)
        if num == 0:
            break
    return lista

def listainvertida(lista):  # devuelve la lista invertida
    print("Lista original:", lista)
    invertida = []
    # todo
    for i in range(len(lista) - 1, -1, -1):
        invertida.append(lista[i])
    return invertida

# Programa principal
listainicial = obtengolista()
listainversa = listainvertida(listainicial)
print("Lista invertida:", listainversa)
