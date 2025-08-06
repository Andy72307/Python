print("*** Generación Ticket de Venta ***")

precio_leche = float(input("Precio Leche: "))
precio_pan = float(input("Precio Pan: "))
precio_lechuga = float(input("Precio Lechuga: "))
precio_platanos = float(input("Precio platanos: "))
descuento = int(input("¿Aplicar algun descuento (%)?: "))

#Cálculo del subtotal (sin impuestos)
subtotal = precio_leche + precio_pan + precio_platanos + precio_lechuga
compra_descuento = subtotal * (descuento/100)
subtotal2 = subtotal - compra_descuento
#Cálculo con impuestos (16%)
impuesto = subtotal2 * 0.16

#Cálculo total de la compra (con impuestos)
costo_total = subtotal2 + impuesto
print(f'''
Subtotal: ${subtotal:.2f}
Descuento: ${compra_descuento} ({descuento}%)
Subtotal con descuento: ${subtotal2}
Impuesto (16%): ${impuesto:.2f}
Costo total de la compra: ${costo_total:.2f}''')