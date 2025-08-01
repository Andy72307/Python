costo_N = 10
costo_I = 20

destino = input("¿El destino del paquete es nacional o internacional? ")
peso = float(input("Ingrese el peso del paquete (kg): "))
destino = destino.strip().lower()
costo = None
if destino == 'nacional':
    costo = costo_N * peso
elif destino == 'internacional':
    costo = costo_I * peso
else:
    print("Destino no valido. Ingresa el valor de nacional o internacional")

if costo is not None:
    print(f'El costo del envio es: ${costo:.2f}')