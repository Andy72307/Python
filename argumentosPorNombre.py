print("*** Funcion con argumentos por nombre ***")

def imprimirPersona(nombre, apellido = '', edad = 0):
    print(f'La persona: {nombre} {apellido} tiene {edad} años')

# Llamar la funcion pasando los argumentos de manera posicional
imprimirPersona('Andres', 'Lagos', 18)

# Llamar la funcion usando argumentos por nombre
imprimirPersona(nombre = 'Juan', apellido = "Leon", edad = 19)

# Llamar la funcion usando argumentos por nombre, pero intercambiando el orden
imprimirPersona(edad = 48, nombre = "Sandra", apellido = 'Ballesteros')

# Argumentos con valor por default
imprimirPersona(nombre = 'Miguel')
imprimirPersona(nombre = 'Miguel', apellido = 'Lagos')
imprimirPersona(apellido = 'Lagos', nombre = 'Miguel')