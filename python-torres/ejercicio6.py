import math

# ejercicio 6
diametro = float(input("Ingrese el diámetro de la esfera: "))

radio = diametro / 2

volumen = (4/3) * math.pi * (radio ** 3)

print(f"El volumen de la esfera con diámetro {diametro} es: {volumen:.2f} unidades cúbicas")
