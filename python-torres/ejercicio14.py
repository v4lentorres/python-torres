# Ejercicio 14
dias = int(input("Ingrese la cantidad de días: "))

meses_por_dias = {
    28: ["Febrero"],
    30: ["Abril", "Junio", "Septiembre", "Noviembre"],
    31: ["Enero", "Marzo", "Mayo", "Julio", "Agosto", "Octubre", "Diciembre"]
}

posibles_meses = meses_por_dias.get(dias, [])

if posibles_meses:
    print(f"Posibles meses con {dias} días: {', '.join(posibles_meses)}")
else:
    print("No se encontraron meses con la cantidad de días ingresada.")
