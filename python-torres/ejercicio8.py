#ejercicio 8

nota_mara = float(input("Ingrese la nota de Mara: "))
nota_juan = float(input("Ingrese la nota de Juan: "))

regalo_mara = ""
regalo_juan = ""

def determinar_regalo(nota):
    if nota < 6:
        return "Ningún regalo"
    elif 6 <= nota <= 7:
        return "Comida en un bar a elegir"
    elif 7 < nota <= 9:
        return "Ropa a elección"
    elif nota == 10:
        return "Comida en un bar a elegir y ropa a elección"

regalo_mara = determinar_regalo(nota_mara)
regalo_juan = determinar_regalo(nota_juan)

print(f"Regalo de Mara: {regalo_mara}")
print(f"Regalo de Juan: {regalo_juan}")
