#corregido

dinero = float(input("Introduce el dinero máximo que te quieres gastar en la compra: "))
productos = []
precios = []
total = 0
contador = 1

while True:
    print("PRODUCTO: ", contador)
    nomp = input("Introduce nombre del producto: ")
    prc = float(input("Introduce el precio del producto: "))

    if total + prc > dinero:
        print("La suma de los precios superó el importe máximo (" + str(dinero) + " € )")
        break

    productos.append(nomp)
    precios.append(prc)
    total += prc
    contador += 1

print("Lista dentro de presupuesto:")
for i in range(len(productos)):
    print("- " + productos[i] + ": " + str(precios[i]) + " €")

print("Importe máximo a gastar: " + str(dinero) + " €")
print("Coste total de la cesta: " + str(total) + " €")

# Menú de opciones
while True:
    print("Opciones:")
    print("S: Calcular dinero sobrante")
    print("R: Eliminar un producto y su precio de la lista")
    print("C: Mostrar productos cuyo precio es mayor que un importe dado")
    print("X: Salir")
    opcion = input("Introduce una opción: ").upper()

    if opcion == "S":
        sobrante = dinero - total
        print("Dinero sobrante: " + str(round(sobrante, 2)) + " €")

    elif opcion == "R":
        print("Productos actuales:")
        for i in range(len(productos)):
            print("[" + productos[i] + ", " + str(precios[i]) + " €]")

        pr = input("Introduce el nombre del producto que quieres eliminar: ")
        if pr in productos:
            idx = productos.index(pr)
            confirm = input("¿Seguro que lo quieres eliminar? (S/N): ").upper()
            if confirm == "S":
                total -= precios[idx]
                productos.pop(idx)
                precios.pop(idx)
                print("Producto eliminado.")
        else:
            print("Producto no encontrado.")

    elif opcion == "C":
        imp = float(input("Introduce el importe límite: "))
        lista = []
        for i in range(len(precios)):
            if precios[i] > imp:
                lista.append((productos[i], precios[i]))
        print("Productos con precio superior al importe dado:")
        for prod, precio in lista:
            print("- " + prod + ": " + str(precio) + " €")

    elif opcion == "X":
        print("Saliendo del programa.")
        break

    else:
        print("Opción inválida.")
