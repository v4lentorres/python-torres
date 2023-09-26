#ejercicio 3

sueldo_basico = float(input("Ingrese el sueldo básico del empleado: "))
asistencia_perfecta = 40000
horas_extra = float(input("Ingrese la cantidad de horas extra trabajadas: "))
jubilacion_descuento = 0.11
obra_social_descuento = 0.02
antiguedad_anos = int(input("Ingrese la antigüedad en años del empleado: "))
antiguedad_bonus = 8000 * antiguedad_anos


salario_bruto = sueldo_basico + asistencia_perfecta + (horas_extra * 5000) + antiguedad_bonus

descuento_jubilacion = salario_bruto * jubilacion_descuento
descuento_obra_social = salario_bruto * obra_social_descuento

salario_neto = salario_bruto - descuento_jubilacion - descuento_obra_social

print("\nBoleta de Liquidación de Haberes")
print("=================================")
print(f"Sueldo Básico: ${sueldo_basico:.2f}")
print(f"Asistencia Perfecta: ${asistencia_perfecta:.2f}")
print(f"Horas Extra ({horas_extra} horas): ${horas_extra * 5000:.2f}")
print(f"Antigüedad ({antiguedad_anos} años): ${antiguedad_bonus:.2f}")
print("=================================")
print(f"Salario Bruto: ${salario_bruto:.2f}")
print(f"Descuento Jubilación ({jubilacion_descuento*100}%): ${descuento_jubilacion:.2f}")
print(f"Descuento Obra Social ({obra_social_descuento*100}%): ${descuento_obra_social:.2f}")
print("=================================")
print(f"Salario Neto: ${salario_neto:.2f}")
print("=================================")
