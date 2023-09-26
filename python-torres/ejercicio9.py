# Ejercicio 9
segundos_totales = int(input("Ingrese la cantidad de segundos: "))

horas = segundos_totales // 3600  # 1 hora = 3600 segundos
segundos_totales %= 3600

minutos = segundos_totales // 60  # 1 minuto = 60 segundos
segundos = segundos_totales % 60

print(f"{segundos_totales} segundos equivalen a:")
print(f"{horas} horas, {minutos} minutos y {segundos} segundos.")
