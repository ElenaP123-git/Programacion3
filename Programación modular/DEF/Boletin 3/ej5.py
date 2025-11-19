def estaOrdenadaAscendentemente(lista):
    """
    4. Verifica si una lista está ordenada ascendentemente.
    """
    if len(lista) <= 1:
        return True
    
    i = 0
    while i < len(lista) - 1:
        if lista[i] > lista[i+1]:
            return False
        i = i + 1
        
    return True

def estaOrdenada(lista, ascendente=True):
    """
    5. Verifica si una lista está ordenada de forma ascendente o descendente.
    """
    if len(lista) <= 1:
        return True

    i = 0
    if ascendente:
        # a. Orden Ascendente
        while i < len(lista) - 1:
            if lista[i] > lista[i+1]:
                return False
            i = i + 1
        return True
    else: 
        # b. Orden Descendente
        while i < len(lista) - 1:
            if lista[i] < lista[i+1]:
                return False
            i = i + 1
        return True

def ejecutar_pruebas_ejercicio_5():
    lista_ascendente = [10, 20, 30, 30]
    lista_descendente = [50, 40, 30, 10]
    lista_desordenada = [1, 5, 3, 9]

    print("--- PRUEBAS DE LA FUNCIÓN estaOrdenada ---")
    
    # Caso 5.a: Ascendente=True (Debe ser True)
    resultado_a = estaOrdenada(lista_ascendente, ascendente=True)
    print("1. Lista ascendente [10, 20, 30, 30], ascendente=True: **" + str(resultado_a) + "**")
    
    # Caso 5.b: Ascendente=False (Debe ser True)
    resultado_b = estaOrdenada(lista_descendente, ascendente=False)
    print("2. Lista descendente [50, 40, 30, 10], ascendente=False: **" + str(resultado_b) + "**")
    
    # Caso 5.c: Desordenada, Ascendente (Debe ser False)
    resultado_c1 = estaOrdenada(lista_desordenada, ascendente=True)
    print("3. Lista desordenada [1, 5, 3, 9], ascendente=True: **" + str(resultado_c1) + "**")
    
    # Caso 5.c: Desordenada, Descendente (Debe ser False)
    resultado_c2 = estaOrdenada(lista_desordenada, ascendente=False)
    print("4. Lista desordenada [1, 5, 3, 9], ascendente=False: **" + str(resultado_c2) + "**")
    
# ejecutar_pruebas_ejercicio_5()