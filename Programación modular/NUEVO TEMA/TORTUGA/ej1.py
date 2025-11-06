def obtiene_datos_de_entrada():
    numero = int(input("Dame un número positivo: "))
    while numero < 0:
        numero = int(input("Dameun número positivo :/ : "))
    return numero
entrada = obtiene_datos_de_entrada()
print(entrada + 4)