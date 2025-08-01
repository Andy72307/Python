mi_lista = [1, 2, 3, 4, 5]
print(f'{mi_lista} -> Lista original')

print(f'{len(mi_lista)}')

print(f'Accedemos al valor del indice 4: {mi_lista[4]}')
print(f'Accedemos al ultimo indice de la lista: {mi_lista[-1]}')

mi_lista[1] = 10

print(f'{mi_lista} -> Lista modificada')

mi_lista.append(6)
print(f'{mi_lista} -> Lista modificada')

mi_lista.insert(2, 15)
print(f'{mi_lista} -> Lista modificada')

mi_lista.remove(5)
print(f'{mi_lista} -> Lista modificada')

mi_lista.pop(1)
print(f'{mi_lista} -> Lista modificada')

del  mi_lista[2]
print(f'{mi_lista} -> Lista modificada')

sublista = mi_lista[1:3]
print(sublista)