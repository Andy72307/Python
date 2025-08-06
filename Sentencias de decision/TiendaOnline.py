print("*** TIENDA EN LINEA ***")

compra_minima = 1000
compra = float(input("Ingrese el precio total de la compra: "))
descuento = 0
miembro = input("¿Es miembro de la tienda (Si/No)? ")
i = miembro.strip().lower()

if compra > compra_minima and i == 'si':
    descuento = 0.1
elif i == 'si':
    descuento = 0.05
elif compra > compra_minima:
    descuento = 0.03
else:
    descuento = 0
if descuento != 0:
    compra_descuento = compra * descuento
    compra_total = compra - compra_descuento
    print(f'''Felicidades, has obtenido un descuento del {descuento * 100:.0f}%
Valor de la compra: ${compra:.2f}
Descuento de la compra: ${compra_descuento:.2f}
Valor final de la compra: ${compra_total:.2f}''')
else:
    print(f'\nNo obtuviste ningun tipo de descuento')
    print(f'Te invitamos a hacerte miembro de la tienda')
    print(f'Valor final de la compra: ${compra:.2f}')