def estaOrdenadaAscendentemente(lista):
    """Verifica si una lista está ordenada ascendentemente."""
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
    Verifica si una lista está ordenada ascendentemente (True) o 
    descendentemente (False).
    """
    if len(lista) <= 1:
        return True

    i = 0
    if ascendente:
        # Orden Ascendente: [i] <= [i+1]
        while i < len(lista) - 1:
            if lista[i] > lista[i+1]:
                return False
            i = i + 1
        return True
    else: # Descendente
        # Orden Descendente: [i] >= [i+1]
        while i < len(lista) - 1:
            if lista[i] < lista[i+1]:
                return False
            i = i + 1
        return True