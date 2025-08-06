print("*** Bienvenido a la aplicación de Salud y Fitness ***")
#Constantes
Meta_Pasos = 10000
calorias = 0.04
#Variables
nombre = input("Ingrese su nombre de usuario: ")
pasos = int(input("Ingrese los pasos que dio el dia de hoy: "))
#Operaciones
calorias_quemadas = pasos * calorias
meta = 'Si' if pasos >= Meta_Pasos else 'No'

print(f''' 
su nombre es: {nombre}
La meta de pasos es: {Meta_Pasos} pasos
Las calorias que quema cada paso son: {calorias} Kcal
la cantidad de pasos que dio fue: {pasos}
las calorias quemadas fueron {calorias_quemadas} Kcal
¿cumplio la meta de pasos? {meta}
''')