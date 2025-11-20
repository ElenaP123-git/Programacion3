def cargaelementos():
    esnumero = True
    listaelementos = []
    while esnumero:
        numeros = input("Introduce un número: ")
        for i in numeros:
            if i not in "0123456789":
                esnumero = False
        if esnumero:
            listaelementos.append(int(numeros))
    return listaelementos
def estaOrdenadaAsc(lista):
    orden = True
    i = 0
    while i < len(lista)-1 and orden:
        if lista[i] > lista [i + 1]:
            orden = False
        i = i + 1
    return orden
def estaordenada(lista,ascendente):
    if ascendente:
        print("Está ordenada ascendentemente")
    else:
        print("No está ordenada ascendentemente")

lista1 = cargaelementos()
print(lista1)
ascendente = estaordenada(lista1)
estaordenada(lista1, ascendente)