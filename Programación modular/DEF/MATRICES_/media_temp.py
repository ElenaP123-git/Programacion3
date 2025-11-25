def calcula(lista_numeros):
    media = 0
    for numero in lista_numeros: # "para cada número en una fila"
        media = numero + media # se suma cada número de la fila
    media = media /len(lista_numeros)
    return media

def calc_media_fila(matriz):# necesito la matriz de fuera 
    lista_media = []
    for fila in matriz: # "para cada fila en la matriz"
        media_fila = calcula(fila) # calcula la media de cada fila
        lista_media.append(media_fila) 
    return lista_media

def media_hotel(lista_media):
    temp_hotel = 0
    for medias in lista_media: # para cada media de la lista de medias
        temp_hotel = temp_hotel + medias # suma las medias 
    temp_hotel = temp_hotel/len(lista_media) # media
    return "Temperatura media del hotel:", temp_hotel

def get_columna(num_columna, matriz):
    columna = []
    for i in range (len(matriz)): # del 0 al 4
        columna.append(matriz[i][num_columna])
    return columna

def calcula_media_column(matriz): # corregido
    columna0 = get_columna(0,matriz)
    return calcula(columna0)
    
def calcula_media_col_det(matriz,num_columna):
    columna = get_columna(num_columna,matriz)
    return calcula(columna)

def calcula_med_por_hab(matriz):
    num_habitaciones = len(matriz[0]) #num de columnas
    lista_medias = []
    for col in range(num_habitaciones):
        media_col = calcula_media_col_det(matriz,col)
        lista_medias.append(media_col)
    return lista_medias

matriz = [
[22,20,19,21],
[18,25,23,22],
[19,21,20,24],
[17,23,22,19],
[24,23,27,26]
]
lista_numeros = matriz[0] # o [22,20,19,21]
resultado = calcula(lista_numeros)
print(resultado)

lista_media = calc_media_fila(matriz) # lista de lista de números
print(lista_media)

temp_hotel = media_hotel(lista_media)
print(temp_hotel)

# Columna 0
print("Columna 0:", get_columna(0, matriz))

# Media columna 0
print("Media columna 0:", calcula_media_column(matriz))

# Media columna determinada (ejemplo columna 2)
print("Media columna 2:", calcula_media_col_det(matriz, 2))

# Lista de medias por habitación (por columnas)
print("Medias por habitación:", calcula_med_por_hab(matriz))
