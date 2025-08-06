productos = [
    ('POO1', 'Camiseta', 20.00),
    ('P002', 'Jeans', 30.00),
    ('P003', 'Sudadera', 40.00)
]

precio_total = 0

print(f'Informacion de los productos: ')

for i in productos:
    id, descripcion, precio = i
    print(f'''
Id: {id}
descrpcion: {descripcion}
precio: ${precio}''')
    precio_total += precio
print(f'\n El precio total es: ${precio_total:.2f}')