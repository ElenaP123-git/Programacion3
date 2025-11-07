def calccadena(pos1,pos2,numero):
    salida1 = numero[pos1] + numero[pos2]
    # print(salida1)
    return salida1, "hola"
cadena = input("dame una cadena")
num = int(cadena)
salida = ""

while len(cadena) <= 4:
    cadena = input("dame una cadena")

    if num % 2 == 0:
        #salida = cadena[2] + cadena[4]
        output = calccadena(2,4,cadena)
        print(output)

    elif num % 3 == 0:
        # salida = cadena[1] + cadena[2]
        calccadena(1,3,cadena)
    
    elif num % 7 == 0:
        # salida = cadena[0] + cadena[3]
        calccadena(0,3,cadena)