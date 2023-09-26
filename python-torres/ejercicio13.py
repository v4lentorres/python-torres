# Ejercicio 13
def tipo_de_triangulo(a, b, c):
    if a == b == c:
        return "equilátero"
    elif a == b or b == c or a == c:
        return "isósceles"
    else:
        return "escaleno"

a = float(input("Ingrese la longitud del primer segmento (a): "))
b = float(input("Ingrese la longitud del segundo segmento (b): "))
c = float(input("Ingrese la longitud del tercer segmento (c): "))

if a + b > c and a + c > b and b + c > a:
    tipo = tipo_de_triangulo(a, b, c)
    print(f"Se forma un triángulo {tipo}.")
else:
    print("No es posible formar un triángulo con estas longitudes.")
