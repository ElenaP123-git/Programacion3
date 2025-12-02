ventas = [
    ["Portátil", 150, 799.99, 4.5],
    ["Smartphone", 250, 599.99, 4.3],
    ["Auriculares", 400, 49.99, 4.0],
    ["Tablet", 120, 299.99, 3.9],
    ["Monitor", 180, 199.99, 4.2],
    ["Smartwatch", 220, 149.99, 4.1],
    ["Teclado mecánico", 300, 89.99, 4.4],
    ["Ratón gaming", 350, 59.99, 4.0],
    ["Cámara digital", 90, 999.99, 4.6],
    ["Consola", 200, 399.99, 4.7]
]
# nombre, nºventa, precio, valoración

def lista_prod(ventas):
    lista_prd= []
    for producto in ventas:
        lista_prd.append(producto[0]) # cómo me funciona esto? what
    return lista_prd 

resultado1 = lista_prod(ventas)
print("La lista de productos es:", resultado1)

def calcular_ingresos(ventas, nombre):
    for producto in ventas:
        if nombre == producto[0]:
            nVenta = producto[1]
            precio = producto [2]
            ingresos = nVenta * precio
    return ingresos

resultado2 = calcular_ingresos(ventas)
print(resultado2)

nombre = ("Introduce el nombre del producto para calcular ingresos: ")
