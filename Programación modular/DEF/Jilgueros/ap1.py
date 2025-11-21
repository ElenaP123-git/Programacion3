def genera_lista():
    lista = []
    return lista

def es_valida(lista):
    esV = True
    if len(lista) == 0:
        print("No se introdujeron notas")
    else:
        minimo = min(lista)
        maximo = max(lista)

    return esV

def calcular_puntos(lista):
    puntos = 0
    return puntos

lista_notas = genera_lista()
if es_valida(lista_notas):
    puntos = calcular_puntos(lista_notas)
    print("Secuencia válida, Nº de puntos:", puntos)
else:
    print("Secuencia de notas no válida")