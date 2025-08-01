print('*** Obtener coordenadas x, y, z ***')

# Definir la funcion
def obtenerCoordenadas():
    x, y, z = 10, 20, 30
    return (x, y, z)

# Llamar la funcion
res = obtenerCoordenadas()

# Unpacking de la tupla
x, y, z = res

print(f'Coordenada x: {x}, coordenada y: {y}, coordenada z: {z}')