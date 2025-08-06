mi_set = {1, 2, 3, 4, 5, 4}
print(f'Mi set: {mi_set}')
#Añadir elementos
mi_set.add(6)
mi_set.add(7)
mi_set.add(3)
print(f'Mi set modificado: {mi_set}')
#Eliminar elementos
mi_set.remove(4)
print(f'Mi set modificado 2: {mi_set}')

#Iterar elementos
for i in mi_set:
    print(i, end=' ')

#Comprobar si existe un elemento en el set
print(f'\nExiste el valor de 1 en el set? {1 in mi_set}')

#Obtener la longitud del set
print(f'Longitud del conjunto: {len(mi_set)}')