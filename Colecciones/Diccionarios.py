# Creamos un dict de persona con clave y valor
persona = {
    'nombre': 'Sergio',
    'edad': 30,
    'pais': 'Mexico'
}
print(f'Diccionario de persona: {persona}')

# Acceder a los elementos del diccionario
print(f'Nombre: {persona['nombre']}')
print(f'Edad: {persona.get('edad')}')
print(f'Pais: {persona.get('pais')}')