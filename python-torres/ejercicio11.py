# Ejercicio 11
total_niños = 50

solo_fresa = 10

solo_chocolate = 5

ningun_helado = 20

al_menos_uno = total_niños - ningun_helado

ambos_helados = solo_fresa + solo_chocolate

helado_fresa = al_menos_uno - solo_chocolate

helado_chocolate = al_menos_uno - solo_fresa

print(f"A {ambos_helados} niños les gusta ambos helados.")
print(f"A {helado_fresa} niños les gusta el helado de fresa.")
print(f"A {helado_chocolate} niños les gusta el helado de chocolate.")
