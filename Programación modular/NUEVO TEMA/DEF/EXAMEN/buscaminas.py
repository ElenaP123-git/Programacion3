import random
def menu():
    print("T) Genera un tablero")
    print("J) Jugar")
    print("E) Salir del juego")
    
def leeyvalidaMenu():
    menu()
    opcion = input("Dime una opcion del menu(T/J/E):")
    while opcion != "T" and opcion != "J" and opcion !="E":
        opcion = input("Dime una opcion del menu válida (T/J/E):")
    while opcion != "E":
        if opcion == "T":
            resultados = cargaTablero()
        elif opcion == "J":
            juega(resultados[0,resultados[1]])
        menu()
        opcion = input("Dime una opcion del menu(T/J/E):")
    ejecutaTerminal()

def cargaTablero():
    tablero = []
    minas = 0
    for i in range (0,8):
        aleatorio = random.randint(0,1)
        if aleatorio == 0:
            tablero.append("")
        elif aleatorio == 1:
            tablero.append("X")
            minas +=1
    print("Tablero generado: ",tablero)
    print("Se han escondido", minas, "minas")
    return tablero,minas

def juega (tablero,minas):
    print("Jugando")
    puntuacion = 0
    historico=[]
    usuario = int(input("Introduce una posición (1-8)"))
    while usuario >8:
        usuario = int(input("Introduce una posición válida: "))
        if usuario in historico:
            print("Posicion revisada")
        else:
            historico.append(usuario)
            if tablero[usuario] == "X":
                puntuacion +=1
                minas = -1
                print("MINA!! Puntuación:", puntuacion,"Minas restantes:",minas)
        print("Has encontrado todas las minas :))")
        print("Tu puntuación final es: ", puntuacion)
        return
    
    def ejecutaTeminal():
        print("Saliendo del programa")

leeyvalidaMenu()