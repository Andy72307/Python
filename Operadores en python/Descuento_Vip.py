from os import times

print("*** Sistema de descuentos VIP ***")
n_productos, cantidad = 10, int(input("¿Cuantos productos compraste hoy?"))
membresia = input("¿Tienes la membresia de la tienda(Si/No)?")

es_elegible = cantidad >= n_productos and membresia.strip().lower() == 'si'

print(f'¿Tienes acceso al descuento VIP? {es_elegible}')