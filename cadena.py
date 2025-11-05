cadena = input("Introduce una cadena que tenga 4 carateres: ")
salida = ""

while len(cadena) <= 4:
        cadena = input("Introduce una cadena que tenga 4 caracteres: ")

if cadena % 2 == 0:               
    salida = cadena[2] + cadena[4]

elif cadena % 3 == 0:
      salida = cadena[1] + cadena[3]

elif cadena % 7 == 0:
      salida = cadena[0] + cadena[3]

print(salida)
