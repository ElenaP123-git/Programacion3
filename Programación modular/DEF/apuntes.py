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

def saludar():
    nombre = "Elena"
    print("Hola", nombre)

saludar()  # → Hola Elena

# MUTABLES E INMUTABLES
def suma(n1, n2):
    n1 = n1+1 # no sirve
    return n1+n2
n1 = 2 # n1 = 2 porque está fuera de la función n1 = n1 + n2
n2 = 3
print(suma(n1,n2)) # utiliza el return n1 + n2
print(n1)   


def suma(n1, n2):
    n1.insert(0, n2)
    return n1 # [3,2,3,4]
n1 = [2, 3, 4] # las listas son mutables, las variables (como arriba), no
n2= 3
print(suma(n1,n2))
print(n1)
