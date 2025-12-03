def pedir_dinero():  # Función que pide al usuario cuánto dinero quiere gastar
    return float(input("Introduce el dinero máximo que te quieres gastar en la compra: "))  

def agregar_productos(dinero):  # Función para añadir productos sin pasarse del dinero
    productos = []  
    precios = []    
    total = 0       # Suma total de lo que llevas gastado
    contador = 1    
    seguir = True   

    while seguir:  # Mientras no te hayas pasado del dinero
        print("PRODUCTO: ", contador)  
        nomp = input("Introduce nombre del producto: ")  
        prc = float(input("Introduce el precio del producto: ")) 

        if total + prc > dinero:  
            print("La suma de los precios superó el importe máximo (" + str(dinero) + " € )")  
            seguir = False  
        else:
            productos.append(nomp) 
            precios.append(prc)     
            total += prc            # Suma el precio al total
            contador += 1           # Pasa al siguiente producto

    return productos, precios, total  # Devuelve las listas y el total gastado “Aquí tienes los resultados que calculé, úsalos donde los necesites” (cálculo arriba)

def mostrar_lista(productos, precios): 
    print("Lista dentro de presupuesto:")
    for i in range(len(productos)):  # Recorre la lista
        print("- " + productos[i] + ": " + str(precios[i]) + " €")  

def mostrar_resumen(dinero, total):  
    print("Importe máximo a gastar: " + str(dinero) + " €")
    print("Coste total de la cesta: " + str(total) + " €")

def calcular_sobrante(dinero, total):
    sobrante = dinero - total   
    sobrante = int(sobrante * 100) / 100 # 2 decimales
    print("Dinero sobrante: " + str(sobrante) + " €")

def eliminar_producto(productos, precios):  
    print("Productos actuales:")
    for i in range(len(productos)):  
        print("[" + productos[i] + ", " + str(precios[i]) + " €]")

    pr = input("Introduce el nombre del producto que quieres eliminar: ")  
    if pr in productos:  
        idx = productos.index(pr)  # Busca su posición
        confirm = input("¿Seguro que lo quieres eliminar? (S/N): ").upper()  
        if confirm == "S":
            productos.pop(idx)  # Elimina el nombre
            precios.pop(idx)    # Elimina el precio correspondiente
            print("Producto eliminado.")
        else:
            print("Cancelado.") 
    else:
        print("Producto no encontrado.")  

    return productos, precios  # Devuelve las listas actualizadas

def mostrar_mayores(productos, precios):  
    imp = float(input("Introduce el importe límite: "))  
    lista = []
    for i in range(len(precios)):  
        if precios[i] > imp:  # Si alguno de los precios es mayor que el importe
            lista.append((productos[i], precios[i]))  # Añade a la lista

    print("Productos con precio superior al importe dado:")
    for i in range(len(lista)):
        prod = lista[i][0]      # Primer elemento de la tupla        # KE
        precio = lista[i][1]    # Segundo elemento de la tupla
        print(prod)
        print(precio)

def menu_opciones(dinero, productos, precios, total):  # Menú para hacer más acciones      #OJO
    salir = False  # Controla si el usuario quiere salir
    while not salir:                                                                  
        print("Opciones:")
        print("S: Calcular dinero sobrante")
        print("R: Eliminar un producto y su precio de la lista")
        print("C: Mostrar productos cuyo precio es mayor que un importe dado")
        print("X: Salir")
        opcion = input("Introduce una opción: ").upper()  

        if opcion == "S":
            calcular_sobrante(dinero, total)  # Calcula lo que sobra

        elif opcion == "R":
            productos, precios = eliminar_producto(productos, precios)  # Elimina producto
            total = sum(precios)  # Recalcula el total

        elif opcion == "C":
            mostrar_mayores(productos, precios)  # Muestra productos caros

        elif opcion == "X":
            print("Saliendo del programa.")
            salir = True  # Termina el bucle

        else:
            print("Opción inválida.")  # Si no es una opción válida

# Programa principal (LO PONE TOODO EN MARCHA)
dinero = pedir_dinero()  # Pide el dinero
productos, precios, total = agregar_productos(dinero)  # Añade productos
mostrar_lista(productos, precios)  # Muestra lo que compraste
mostrar_resumen(dinero, total)  # Muestra resumen
menu_opciones(dinero, productos, precios, total)  # Abre el menú de opciones
