# Una función es un bloque de código que se puede REUTILIZAR
def nombre_funcion(parametros):
    # código que hace algo
    return resultado

# Ejemplo básico
def suma(a, b):
    return a + b

print(suma(3, 4))  # Resultado: 7
# Aquí solo se imprime, no se guarda en una variable.
# Si quiero reutilizarlo, debo guardarlo:
resultado = suma(3, 4)
print(resultado)       # 7
print(resultado * 2)   # 14


# Función dentro de otra
def cuadrado_suma(a, b):
    return suma(a, b) ** 2  # usamos la función suma dentro de otra

print(cuadrado_suma(2, 3))  # (2+3)^2 = 25


# MATRICES (listas de listas)
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Acceso por índices:
# matriz[0] → [1, 2, 3] (primera fila)
# matriz[1] → [4, 5, 6] (segunda fila)
# matriz[0][0] → 1 (fila 1, columna 1)
# matriz[1][2] → 6 (fila 2, columna 3)

# COLUMNAS
mA = [[1, 2],
      [3, 4]]
columna_0 = [fila[0] for fila in mA]  # primera columna [1, 3]
columna_1 = [fila[1] for fila in mA]  # segunda columna [2, 4]

print(columna_0)  # [1, 3]
print(columna_1)  # [2, 4]


# Recorrer toda la matriz
for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")
    print()  # salto de línea al final de cada fila (forma matriz)


# EJEMPLOS TÍPICOS DE EXAMEN

# SUMAR TODOS LOS ELEMENTOS
def suma_matriz(matriz):
    total = 0
    for fila in matriz:
        for elemento in fila:
            total += elemento
    return total

print(suma_matriz([[1, 2], [3, 4]]))  # Resultado: 10


# ENCONTRAR EL MAYOR ELEMENTO
def max_matriz(matriz):
    mayor = matriz[0][0]  # primer elemento como punto de partida
    for fila in matriz:
        for elemento in fila:
            if elemento > mayor:
                mayor = elemento
    return mayor

print(max_matriz([[5, 8], [2, 9]]))  # Resultado: 9


# TRANSPONER MATRIZ (intercambiar filas por columnas)
def transponer(matriz):
    filas = len(matriz) # 2 filas
    columnas = len(matriz[0]) # 3 columnas en primera fila
    nueva = []
    for j in range(columnas): # recorre columnas (0,1,2) j = columna dentro de fila
        fila_nueva = []
        for i in range(filas): # recorre filas (0,1) i = fila
            fila_nueva.append(matriz[i][j]) 
        nueva.append(fila_nueva)
    return nueva

print(transponer([[1, 2, 3], [4, 5, 6]]))  # Resultado: [[1,4],[2,5],[3,6]]

# EXPLICACIÓN ARRIBA [][]
# j = 0 (primera columna):
#   i = 0 → matriz[0][0] = 1 (fila 1 col 1...)
#   i = 1 → matriz[1][0] = 4 → fila nueva = [1, 4] (fila 2 columna 1...)

# j = 1 (segunda columna):
#   i = 0 → matriz[0][1] = 2
#   i = 1 → matriz[1][1] = 5 → fila nueva = [2, 5]

# j = 2 (tercera columna):
#   i = 0 → matriz[0][2] = 3
#   i = 1 → matriz[1][2] = 6 → fila nueva = [3, 6]


# FUNCIONES QUE USAN OTRAS FUNCIONES
def media_matriz(matriz):
    total = suma_matriz(matriz)
    cantidad = len(matriz) * len(matriz[0]) # 2 filas x 2 columnas de primera fila
    return total / cantidad

print(media_matriz([[1, 2], [3, 4]]))  # Resultado: 2.5


def resumen_matriz(matriz):
    return {
        "suma": suma_matriz(matriz),
        "media": media_matriz(matriz),
        "maximo": max_matriz(matriz)
    }

print(resumen_matriz([[5, 8], [2, 9]]))
# Resultado: {'suma': 24, 'media': 6.0, 'maximo': 9}


# DIAGONALES
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

def imprimir_diagonales(matrix):
    num_filas_y_col = len(matrix)
    diagonal_principal = [matrix[i][i] for i in range(num_filas_y_col)]
    diagonal_secundaria = [matrix[i][num_filas_y_col -1 -i] for i in range(num_filas_y_col)]
    
    return diagonal_principal, diagonal_secundaria

dp,ds = imprimir_diagonales(matrix)
print("Diagonal principal:", dp)
print("Diagonal secundaria:", ds)