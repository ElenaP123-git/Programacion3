def obtener_cadenas_de_usuario():
    cadenas_str = input("Introduce varias cadenas separadas por comas (ej: manzana,pera,uva,manzana,uva,fresa): ")
    
    # dividir la cadena de entrada por comas
    cadenas_divididas = cadenas_str.split(', ')
    return cadenas_divididas

def construir_lista_sin_repetidos(lista_con_duplicados):
    lista_sin_duplicados = []
    for elemento in lista_con_duplicados:
        if elemento not in lista_sin_duplicados:
            lista_sin_duplicados.append(elemento)
         
    return lista_sin_duplicados

def programa_cadenas_unicas_principal():

    lista_original = obtener_cadenas_de_usuario()
    lista_unica = construir_lista_sin_repetidos(lista_original)
    
    # mostrar los resultados
    print("Lista Original (con posibles duplicados): ", lista_original)
    print("Lista sin Cadenas Repetidas (Usando bucle): **" + str(lista_unica) + "**")

programa_cadenas_unicas_principal()