#ejercicio 2
import random

nombres_participantes = input("Ingresa los nombres de los participantes separados por comas: ")
lista_participantes = nombres_participantes.split(",")

lista_participantes = [nombre.strip() for nombre in lista_participantes]

ganador = random.choice(lista_participantes)

print(f"{ganador} se queda con la mejor parte.")
