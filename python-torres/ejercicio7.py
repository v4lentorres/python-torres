# ejercicio 7
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

if numero2 == 0:
    print("Error: No se puede dividir entre cero.")
else:
    resultado = numero1 / numero2
    print(f"El resultado de la división es: {resultado}")
