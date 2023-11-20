import random

#Función 10 valores enteros aleatorios entre 1 y 20
def generar_lista():
    return [random.randint(1, 20) for _ in range(10)]

# Función para contar cuántos valores en la lista son mayores que un número dado
def contar_mayores(lista, valor):
    return sum(1 for elemento in lista if elemento > valor)

# Función para calcular el promedio de la lista
def calcular_promedio(lista):
    return sum(lista) / len(lista) if len(lista) > 0 else 0

# Función para encontrar el valor más grande y el más pequeño de la lista
def encontrar_extremos(lista):
    if not lista:
        return None, None
    return min(lista), max(lista)

# Generar la lista de valores aleatorios
lista_valores = generar_lista()

# Mostrar la lista
print("Lista de valores:", lista_valores)

# Ingresar un valor
valor_ingresado = int(input("\nIngrese un valor: "))

# Contar_mayores y mostrar el resultado
cantidad_mayores = contar_mayores(lista_valores, valor_ingresado)
print(f"Hay {cantidad_mayores} valores en la lista mayores que {valor_ingresado}.")

# Calcular_promedio y mostrar el resultado
promedio = calcular_promedio(lista_valores)
print(f"El promedio de la lista es: {promedio:.2f}")

# Encontrar_extremos y mostrar los resultados
minimo, maximo = encontrar_extremos(lista_valores)
print(f"El valor más pequeño en la lista es: {minimo}")
print(f"El valor más grande en la lista es: {maximo}")