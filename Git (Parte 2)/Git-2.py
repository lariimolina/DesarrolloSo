def suma(valor1, valor2):
    return valor1 + valor2

def resta(valor1, valor2):
    return valor1 - valor2

def multiplicacion(valor1, valor2):
    return valor1 * valor2

def division(valor1, valor2):
    if valor2 != 0:
        return valor1 / valor2
    else:
        return "Error: No se puede dividir por cero."

while True:
    print("\nMenu:")
    print("1. Ingresar valor 1")
    print("2. Ingresar valor 2")
    print("3. Mostrar suma")
    print("4. Mostrar resta")
    print("5. Mostrar multiplicación")
    print("6. Mostrar división")
    print("7. Salir")

    opcion = input("Elija una opción: ")

    if opcion == '1':
        valor1 = float(input("Ingrese el primer valor: "))
    elif opcion == '2':
        valor2 = float(input("Ingrese el segundo valor: "))
    elif opcion == '3':
        print(f"Suma: {suma(valor1, valor2)}")
    elif opcion == '4':
        print(f"Resta: {resta(valor1, valor2)}")
    elif opcion == '5':
        print(f"Multiplicación: {multiplicacion(valor1, valor2)}")
    elif opcion == '6':
        print(f"División: {division(valor1, valor2)}")
    else: opcion == '7':
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Intente nuevamente.")