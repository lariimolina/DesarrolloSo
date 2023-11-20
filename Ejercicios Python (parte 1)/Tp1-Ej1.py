suma_temperaturas = 0

# For para ingresar temp
for dia in range(1, 6):
    temperatura = float(input(f"Ingrese la temperatura: "))
    suma_temperaturas += temperatura

# Calcular promedio
temperatura_promedio = suma_temperaturas / 5

# Mostrar el resultado
print(f"\nLa temperatura promedio de la semana es: {temperatura_promedio}")