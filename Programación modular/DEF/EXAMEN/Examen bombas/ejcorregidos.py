import random

# Pintar menú inicial
print("T. Genera un nuevo tablero")
print("J. Genera el juego en el tablero")
print("E. Salir del juego")

opcion = input("Selecciona una opcion: ")
while opcion != "T" and opcion != "J" and opcion != "E":
    opcion = input("Selecciona una opcion: ")

resultados = None

while opcion != "E":
    if opcion == "T":
        tablero = []
        minas = 0
        for i in range(8):
            aleatorio = random.randint(0, 1)
            if aleatorio == 0:
                tablero.append("")
            else:
                tablero.append("X")
                minas += 1
        print("Tablero generado. Se han escondido " + str(minas) + " minas. Tablero " + str(tablero))
        resultados = (tablero, minas)

    elif opcion == "J":
        if resultados is None:
            print("Primero debes generar un tablero con la opción T.")
        else:
            tablero = resultados[0]
            minas = resultados[1]
            print("Jugando")
            puntuacion = 0
            historico = []
            while minas != 0:
                usuario = int(input("Introduce una posicion(1-8): "))
                while usuario > 8 or usuario < 1:
                    usuario = int(input("Introduce una posicion válida (1-8): "))
                usuario -= 1  # Ajustar índice a 0-based
                if usuario in historico:
                    print("Posicion revisada")
                else:
                    historico.append(usuario)
                    if tablero[usuario] == "X":
                        puntuacion += 1
                        minas -= 1
                        print("¡MINA! Puntuacion: " + str(puntuacion) + " | MinasRestantes: " + str(minas))
                    else:
                        puntuacion -= 1
                        print("AGUA! Puntuacion: " + str(puntuacion) + " | MinasRestantes: " + str(minas))
            print("¡Has encontrado todas las minas! Tu puntuacion final es: " + str(puntuacion))

    print("T. Genera un nuevo tablero")
    print("J. Genera el juego en el tablero")
    print("E. Salir del juego")
    opcion = input("Selecciona una opcion: ")
    while opcion != "T" and opcion != "J" and opcion != "E":
        opcion = input("Selecciona una opcion: ")

print("Saliendo del programa")
