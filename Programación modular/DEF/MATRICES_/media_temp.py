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
    for i in range (0, len(matriz)): # del 0 al 4
        columna.append(matriz[i][num_columna])
    return columna

def calcula_column_det(matriz, num_columna):
    calcula_columna = get_columna(matriz)
    # ???
    return

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

columna = get_columna(matriz)
print(columna) # ???
