# Ejercicio 1 
humedad = {
    "María": 65,
    "Jorge": 72,
    "Ana": 68
}

promedio_humedad = sum(humedad.values()) / len(humedad)

amigo_que_paga = max(humedad, key=lambda amigo: abs(humedad[amigo] - promedio_humedad))

print(f"{amigo_que_paga} pagará el almuerzo.")
