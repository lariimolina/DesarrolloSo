# Ingresar la cantidad de invitados y el precio por kg
cantidad_invitados = int(input("Ingrese la cantidad de invitados: "))
precio_por_kg = float(input("Ingrese el precio por kilogramo de carne: "))

# Calcular la cantidad total de carne y costo
cantidad_carne_total = cantidad_invitados * 0.7
costo_total = cantidad_carne_total * precio_por_kg

# Mostrar los resultados
print(f"\nFranco debe comprar {cantidad_carne_total:.2f} kg de carne.")
print(f"El costo total será de ${costo_total:.2f}.")