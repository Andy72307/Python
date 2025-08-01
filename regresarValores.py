print("*** Regresar una tupla de valores desde una funcion ***")

# Definicion de la funcion
def personaMayus(nombre, apellido, edad):
    print("f'Esta funcion regresa varios valores(tupla)")
    return (nombre.upper(), apellido.upper(), edad) 

# Programa principal

nombre, apellido, edad = personaMayus('Andres', 'Lagos', 18)
print(f'La persona {nombre} {apellido} tiene {edad} años')