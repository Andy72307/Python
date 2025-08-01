#Conversion de tipos de datos
from email.quoprimime import body_length

#Convertir de cadena a numero
numero_cadena = '10'
numero_entero = int(numero_cadena)
print(f'Valor numerico en cadena: {numero_cadena}')
print(f'Cadena a entero: {numero_entero}')

#Convertir de cadena a flotante
numero_cadena = '3.14'
numero_flotante = float(numero_cadena)
print(f'Cadena a flotantes: {numero_flotante}')

#Convertir de numero a cadena
numero_entero = 25
numero_cadena = str(numero_entero)
print(f'Entero a cadena: {numero_cadena}')

#Convertir a booleano
#Si el valor es 0, cadena vacia, o el valor es None, entonces regresa False
#Regresa True, si el valor es distinto de 0, si es distinto de cadena vacia
#y tambien si es distinto de none
numero_entero = 0
booleano = bool(numero_entero)
print(f'El valor booleano de 0: {booleano}') #False incluye 0, 0.0
numero_flotante = 5
booleano = bool(numero_flotante)
print(f'El valor booleano de 5: {booleano}')

cadena = ''
booleano = bool(cadena)
print(f'Valor booleano de cadena vacia: {booleano}')

cadena = "Hola"
booleano = bool(cadena)
print(f'Valor booleano de cadena no vacia: {booleano}')

variable = None
booleano = bool(variable)
print(f'Valor booleano de None: {booleano}')