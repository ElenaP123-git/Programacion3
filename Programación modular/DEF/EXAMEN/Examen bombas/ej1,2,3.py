opcion = ""
while opcion != "E":
    print("T) Pulse T para generar un nuevo tablero")
    print("J) Pulse J para jugar")
    print("Pulse E para salir del juego")
    print("Elige una opción")
    opcion = input(("Introduce una opción: "))
    if opcion == "T":
        print("Generando tablero...")
    elif opcion == "J":
        print("Jugando")

print("Saliendo...")
print("Fuera del programa")

import random
opcion = ""
while opcion != "E":
    print("T) Pulse T para generar un nuevo tablero")
    print("J) Pulse J para jugar")
    print("E) Pulse E para salir del juego")
    print("Elige una opción")
    opcion = input(("Introduce una opción: ")) . upper()
    if opcion == "T":
        print("Generando tablero...")
        tablero = []
        tableroSigno=[]
        aleatorio = [random.randint(0,1) for i in range (8)] # me va a dar 8 números del 0-1
        tablero.append(aleatorio)
        for i in tablero:
            if i == "0":
                tableroSigno.append(" ")
            elif i == "1":
                tableroSigno.append("X")
        print("¡Tablero generado! Se han escondido 3 minas. Tablero: ", tableroSigno)

    elif opcion == "J":
        print("Jugando")
        
print("Saliendo...")
print("Fuera del programa")


import random
opcion = ""
cont_t =  0

while opcion != "E":
    print("T) Pulse T para generar un nuevo tablero")
    print("J) Pulse J para jugar")
    print("E) Pulse E para salir del juego")
    print("Elige una opción")
    opcion = input(("Introduce una opción: ")) . upper()
    if opcion == "T":
        print("Generando tablero...")
        tablero = []
        aleatorio = [random.randint(0,1) for i in range (8)] # me va a dar 8 números del 0-1
        tablero.append(aleatorio)
        for i in tablero:
            if i == "0":
                tablero.append(" ")
            elif i == "1":
                tablero.append("X")
        print("¡Tablero generado! Se han escondido 3 minas. Tablero: ", tablero)
        cont_t +=1

    elif opcion == "J":
        if cont_t > 0:
            print("Jugando")
            print("Tienes que encontrar 3 minas")
            posicion = int(input("Introduce una posicion (1-8): "))
            for i in len(tablero):
                if posicion in i:
                    print("Caiste en ")
        else:
            print("Tienes que generar antes un tablero (T)")
    
        

print("Saliendo...")
print("Fuera del programa")

# se va a quedar el tablero en 0 y 1