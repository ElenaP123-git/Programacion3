def obtiene_datos_de_entrada():
    numero = int(input("Dame un número positivo: "))
    while numero < 0:
        numero = int(input("Dame un número positivo :/ : "))
    return numero
entrada = obtiene_datos_de_entrada() # variable que evita que pierda la función
print(entrada + 4)