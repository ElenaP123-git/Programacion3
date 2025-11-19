def leer_numeros_y_filtrar_terminados_en_3():
    """Lee 10 números enteros y devuelve una lista con los que terminan en 3."""
    numeros_terminados_en_3 = []
    print("Introduce 10 números enteros:")
    
    contador = 0
    while contador < 10:
        prompt = "Número " + str(contador + 1) + ": "
        
        entrada = input(prompt)
        numero = int(entrada)
        
        if abs(numero) % 10 == 3:
            numeros_terminados_en_3.append(numero)
        
        contador = contador + 1
        
    return numeros_terminados_en_3

# Ejemplo de ejecución:
lista_final = leer_numeros_y_filtrar_terminados_en_3()
# print("Lista de números terminados en 3: " + str(lista_final))