# diagonales
matriz = [[2, 1, 6],
          [3, 5, 7],
          [4, 9, 2]
]
def suma_diagonal_simple(matriz, esPrincipal):
    n = len(matriz)
    suma = 0

    if esPrincipal:
        # Diagonal Principal: i = j
        for i in range(n):
            suma += matriz[i][i]
    else:
        # Diagonal Secundaria: j = n - 1 - i
        for i in range(n):
            j = n - 1 - i
            suma += matriz[i][j]

    return suma

resultado = suma_diagonal_simple(matriz, True)
print(resultado)