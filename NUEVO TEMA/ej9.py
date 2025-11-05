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

entrada = input("Introduce el tiempo total en segundos (ej. 7385): ")
segundos = int(entrada)
print(segundos_a_hms(segundos))