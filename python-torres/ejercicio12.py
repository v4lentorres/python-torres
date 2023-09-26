# Ejercicio 12
numero_mes = int(input("Ingrese el número del mes (1-12): "))

nombres_meses = [
    "Enero",
    "Febrero",
    "Marzo",
    "Abril",
    "Mayo",
    "Junio",
    "Julio",
    "Agosto",
    "Septiembre",
    "Octubre",
    "Noviembre",
    "Diciembre"
]

if 1 <= numero_mes <= 12:
    nombre_mes = nombres_meses[numero_mes - 1]
    print(f"El mes número {numero_mes} es {nombre_mes}.")
else:
    print("Número de mes no válido. Ingrese un número entre 1 y 12.")
