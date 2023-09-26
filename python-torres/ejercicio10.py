# Ejercicio 10
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
numero3 = float(input("Ingrese el tercer número: "))

numeros_iguales = 0

if numero1 == numero2:
    numeros_iguales += 1
if numero1 == numero3:
    numeros_iguales += 1
if numero2 == numero3:
    numeros_iguales += 1

if numeros_iguales == 0:
    print("Los tres números son diferentes.")
elif numeros_iguales == 1:
    print("Hay un par de números iguales.")
elif numeros_iguales == 2:
    print("Hay dos pares de números iguales.")
else:
    print("Los tres números son iguales.")
