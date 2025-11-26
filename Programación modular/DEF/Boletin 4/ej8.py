matriz = [[2,3,4],[1,3,3],[5,5,2]]
def calc_lista_maximos(matriz):
    mayores = []
    for fila in matriz:
        mayor = calcula_maximo(fila)
        mayores.append(mayor)
    return mayores

def calcula_maximo(listanum):
    mayor = listanum[0]
    for numero in listanum:
        if numero > mayor:
            mayor = numero
    return mayor

def get_maxm_por_fila(num_fila,matriz):
    lista_maximos = calc_lista_maximos(matriz)
    return lista_maximos[num_fila]

def max_columna(matriz,col):
    maximo = matriz[0][col]
    for fila in matriz:
        if fila[col] > maximo:
            maximo = fila[col]
    return maximo

def max_total_matriz(matriz):
    max_por_fila = calc_lista_maximos(matriz)
    max_total = calcula_maximo(max_por_fila)
    return max_total

# --- PRUEBAS usando concatenación ---
print("Matriz: " + str(matriz))
print("-" * 20)

# Prueba A
fila_a_probar = 1
max_fila = get_maxm_por_fila(fila_a_probar, matriz)
print("Máximo de la Fila " + str(fila_a_probar) + ": " + str(max_fila))

# Prueba B
columna_a_probar = 0
max_col = max_columna(matriz, columna_a_probar)
print("Máximo de la Columna " + str(columna_a_probar) + ": " + str(max_col))

# Prueba C
max_total = max_total_matriz(matriz)
print("Máximo Total de la Matriz: " + str(max_total))

