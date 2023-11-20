# Ingresar el nombre y la edad del socio
nombre = input("Ingrese el nombre del socio: ")
edad = int(input("Ingrese la edad del socio: "))

# Determinar la categoría
if 13 <= edad <= 15:
    categoria = "Infantil"
elif 15 < edad <= 17:
    categoria = "Cadete"
elif 17 < edad <= 19:
    categoria = "Juvenil"
else:
    categoria = "Mayor"

# Mostrar la categoría
print(f"\nEl socio {nombre} pertenece a la categoría {categoria}.")