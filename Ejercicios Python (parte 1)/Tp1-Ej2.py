# Valor actual de un Bitcoin en Pesos
valor_bitcoin = 6581363

# Solicitar cantidad de bitcoins
cantidad_bitcoins = float(input("Ingrese la cantidad de Bitcoins que posee: "))

# Conversión
equivalente_pesos = cantidad_bitcoins * valor_bitcoin

# Mostrar el resultado
print(f"\n{cantidad_bitcoins} Bitcoins equivalen a {equivalente_pesos} Pesos Argentinos hoy.")