# nombre productos y precios (cargacesta(dineroMax))
def cargacesta(dineroMax):
    productos = []
    precios = []
    costeTotal = 0
    rep = True

    while rep:
        cesta=input("Intruduce el producto: ").upper()
        productos.append(cesta)
        coste=input("Intruduce el coste de su producto: ")
        precios.append(coste)
        total=total+float(coste)
        if float(total)>dineroMax:
                total=total-float(coste)
                lim=precios.index(coste)
                productos.pop(lim)
                precios.pop(lim)
                rep=False

    print("Importe máxigo a gastar:",dineroMax)
    print("Productos:",productos)
    print("Precios:",precios)
    print("Coste total de la cesta:",total)
    return productos,precios,costeTotal

dinero = float(input("Introduce el importe máximo a gastar: "))
resultados = cargacesta(dinero) # LO PIERDO SI NO LO GUARDO EN UNA VARIABLE
productos = resultados[0]
precios = resultados[1]
costeTotal = resultados[2]

# coste total de precios productos y dinero gastado en total
