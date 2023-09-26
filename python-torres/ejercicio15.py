from datetime import datetime

# Ejercicio 15
fecha1_str = input("Ingrese la primera fecha (dd/mm/yyyy): ")
fecha2_str = input("Ingrese la segunda fecha (dd/mm/yyyy): ")

fecha1 = datetime.strptime(fecha1_str, '%d/%m/%Y')
fecha2 = datetime.strptime(fecha2_str, '%d/%m/%Y')

diferencia = abs((fecha2 - fecha1).days)

print(f"Hay {diferencia} días entre {fecha1_str} y {fecha2_str}.")
