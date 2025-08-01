productos = []
contador = int(input("Cuantos productos deseas agregar al invetario? "))
j = 1

for i in range(contador):
    print(f"Ingresa los valores del producto {j}: ")
    nombre = input("Nombre: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))
    j += 1