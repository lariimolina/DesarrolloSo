# Ingresar el monto de la compra
monto_compra = float(input("Ingrese el monto de la compra: "))

# Se aplica descuento?
if monto_compra > 3500:
    # Calcular el descuento del 10%
    descuento = 0.10 * monto_compra

    # Calcular el importe final con descuento
    importe_final = monto_compra - descuento

    # Mostrar con descuento
    print(f"\nImporte final a pagar: ${importe_final:.2f}")
else:
    # Mostrar importe
    print(f"\nImporte final a pagar: ${monto_compra:.2f}")