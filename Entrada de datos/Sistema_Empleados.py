print("*** Sistema de empleados ***")
nombre_empleado = input("Nombre del empleado: ")
edad_empleado = int(input("Edad del empleado: "))
salario_empleado = float(input("Salario del empleado: "))
jefe_departamento = input("¿Es jefe de departamento (Si/No)?: ")

#Convertir a tipo bool la variable jefe_departamento
jefe_departamento = jefe_departamento.lower() == 'si'

# Imprimir los valores del empleado
print('\nDatos del empleado')
print(f'Nombre: {nombre_empleado}')
print(f'Edad: {edad_empleado}')
print(f'Salario: {salario_empleado:.2f}')
print(f'¿Es jefe de departamento? {jefe_departamento}')
