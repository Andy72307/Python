print("*** Funcion con argumentos por nombre ***")

def imprimirPersona(nombre, apellido, edad):
    print(f'La persona: {nombre} {apellido} tiene {edad} años')

# Llamar la funcion pasando los argumentos de manera posicional
imprimirPersona('Andres', 'Lagos', 18)

# Llamar la funcion usando argumentos por nombre
imprimirPersona(nombre = 'Juan', apellido = "Leon", edad = 19)