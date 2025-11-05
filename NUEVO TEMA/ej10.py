def segundos_a_hms(segundos_totales):
    
    # 3600 segundos/hora
    horas = segundos_totales // 3600
    
    # calcular los segundos restantes después de las horas
    segundos_restantes = segundos_totales % 3600
    
    # 60 segundos/minuto
    minutos = segundos_restantes // 60
    
    # calcular segundos finales (el resto de los minutos)
    segundos_finales = segundos_restantes % 60
    
    return horas,"horas", minutos,"minutos", segundos_finales, "segundos"

opcion = ""

while opcion != "-1":
    print("S: Convertir a segundos")
    print("M: Convertir a minutos")
    print("H: Convertir a horas")
    print("-1: Salir del programa")
    opcion = input("Introduzca su elección: ") .upper()
    entrada = input("Introduce el tiempo total en segundos (ej. 7385): ")
    segundos = int(entrada)

    if opcion == "H":
        resultado = segundos_a_hms(segundos)
        print("Desglose: ", str(resultado))

    elif opcion == "M":
        minutos = segundos / 60
        print(" Minutos decimales: ", str(minutos))

    elif opcion == "S":
        print("Ya está en segundos: ", str(segundos))
print("Fin del programa")
