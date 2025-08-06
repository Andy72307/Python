canciones = []
nombre = input("Ingresa el nombre de la playlist: ")
n_canciones = int(input("¿Cuantas canciones deseas agregar? "))

for j in range(n_canciones):
    cancion = input(f'Ingresa la cancion {j + 1}: ')
    canciones.append(cancion)
print()
canciones.sort()
print(f'Playlist {nombre}')
for i in canciones:
    print(f'- {i}')