# diagonales de una matriz
matriz = [[8, 1, 6],
          [3, 5, 7],
          [4, 9, 2]]

def devuelveDiagonal(matriz):
    linea = 0
    posi = 0
    lista = []
    for i in range(len(matriz)):
        lista.append(matriz[linea][posi])
        linea += 1
        posi += 1
    return lista

print(devuelveDiagonal(matriz))


def otraDiagonal(matriz):
    linea = 0
    posi = len(matriz) - 1
    lista = []
    for i in range(len(matriz)):
        lista.append(matriz[linea][posi])
        linea += 1
        posi -= 1
    return lista

print(otraDiagonal(matriz))