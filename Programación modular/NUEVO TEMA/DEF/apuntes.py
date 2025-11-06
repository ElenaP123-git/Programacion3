# def y return
def suma(numero_1, numero_2):
    resultado = numero_1 + numero_2
    return resultado #si no pongo sto, el def no va :,)
print(suma(5,2))
print(suma(5,2),3,4) # Ke?

cadena1 = "me gusta"
cadena2 = " el bacon frito"
print(suma(cadena1,cadena2))

def saludar(nombre = "Desconocido"):
    return "Buenas tardes, señor ", nombre
print(saludar()) # Nombre toma el valor desconocido
print(saludar("Pepe")) # Nombre toma el valor  Pepe

def calcCadena(pas1,pas2,numero):
    salida = numero[pas1] + numero[pas2]
    print(salida)
