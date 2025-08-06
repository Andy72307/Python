# suscriptores = {}  # Aqui se define un diccionario vacio
suscriptores = set()
numero_sub = int(input('Ingresa el numero de suscriptores iniciales: '))
for _ in range(numero_sub):
    suscriptores.add(input('Nuevo suscriptor: '))
print(f'Lista de suscriptores inicial: {suscriptores}')

#Verificar si un nuevo suscriptor ya esta en la lista
nuevo_sub = input('Ingresa un nuevo suscriptor: ')
if nuevo_sub in suscriptores:
    print(f'El nuevo suscriptor ya esta en la lista {nuevo_sub}')
else:
    suscriptores.add(nuevo_sub)
    print(f'El nuevo suscriptor se añadio a la lista {nuevo_sub}')
print(f'Lista de suscriptores final: {suscriptores}')

#Eliminar un suscriptor ya existente
eliminar_sub = input('Ingresa el suscriptor a eliminar: ')
suscriptores.remove(eliminar_sub)
print(f'El suscriptor {eliminar_sub} ha sido eliminado de la lista')
print(f'Lista de suscriptores: {suscriptores}')

# Verificamos la cantidad total de suscriptores
print(f'Cantidad total de suscriptores: {len(suscriptores)}')

# Mostramos todos los suscriptores
print(f'--- Lista de suscriptores ---')
for i in suscriptores:
    print(f'- {i}')