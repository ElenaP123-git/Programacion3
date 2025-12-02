matriz = [
    ['A', 'B', 'C', 'D'],    # Fila 1
    ['E', 'F', 'G', 'H'],    # Fila 2
    ['I', 'J', 'K', 'L'],    # Fila 3
    ['M', 'N', 'Ñ', 'O'],    # Fila 4
    ['P', 'Q', 'R', 'S'],    # Fila 5
    ['T', 'U', 'V', 'W'],    # Fila 6
    ['X', 'Y', 'Z', '_']     # Fila 7  (“_” representa el espacio)
]

cadena = ("21,34,74,21,71,31,61,44,74,34,34,21,23,11,74,13,44,42,74,61,53,11,12,11,32,44,74,72,74,51,21,53,54,31,54,61,21,42,13,31,11")
cadena = cadena.split(",")


def col_filas(cadena,matriz):
    descifrado = []
    for num in (cadena):
        letra=matriz[int(num[0])-1][int(num[1])-1] # se le resta -1 porque la cadena optiene la 1º posición 1,1 pero python lo que lee en la matriz es 0,0
        descifrado.append(letra)
    return descifrado

descifrando=col_filas(cadena,matriz)
print(descifrando)

palabra = ("NO SOLO HAY QUE CONFIAR EN EL PROCESO, HAY QUE SEGUIRLO")

