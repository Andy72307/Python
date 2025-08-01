#Operadores de asignación
numero = 5
print(f'Valor de numero: {numero}')
numero = 10
print(f'Valor de numero: {numero}')
cadena = "Saludos desde Python"
print(f'Valor de la cadena: {cadena}')

#Asignacion multiple
x, y, z = 5, 'Hola', -9.15
print(f'Valor de x: {x}, Valor de y: {y}, Valor de z: {z}')

#Asignacion encadenada
a = b = c = 10
print(f'Valor a: {a}, Valor b: {b}, Valor c: {c}')

#Intercambio de valores de una variable, sin utilizar variables temporales
x, y = 5, 10
print(f'Valor inicial x: {x}, Valor inicial y: {y}')
#Aplicando el concepto de asignacion multiple intercambiamos valores
x, y = y, x
print(f'Valor x: {x}, Valor y: {y}')

#Recibir multiples valores de la entrada del usuario
nombre, apellido = input("Ingresa tu nombre y apellido separado por coma:").split(',')
print(f'Nombre: {nombre}, Apellido:{apellido}')