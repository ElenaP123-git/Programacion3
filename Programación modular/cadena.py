cadena = ""

while len(cadena) <= 4:
    cadena = input("Introduce una cadena con más de 4 caracteres: ")

numero = int(input("Introduce un número: "))

resultado = ""

if numero % 2 == 0 and len(cadena) > 4:
    if len(cadena) > 4:
        resultado += cadena[2] + cadena[4]

if numero % 3 == 0 and len(cadena) > 2:
    resultado += cadena[1] + cadena[2]

if numero % 7 == 0 and len(cadena) > 3:
    resultado += cadena[0] + cadena[3]

print("Resultado:", resultado)
