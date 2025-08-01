from colorsys import yiq_to_rgb

print('Manejo de tuplas')

tupla = (1, 2, 3, 4, 5)

print(tupla)

for i in tupla:
    print(i, end=' ')

#Tupla Eje X, Y
coordenadas = 3, 5
print(f'Coordenada del eje X: {coordenadas[0]} y coordenada eje Y: {coordenadas[1]}')

tupla_unitaria = 10,
print(f'Tupla de un elemento: {tupla_unitaria}')

tupla_anidada = 1, (2, 3), (20, 10)
print(f'Segundo elemnto de la tupla anidada: {tupla_anidada[1]}')