print("Promedio de calificaciones")

calificaciones = []

n_calificaciones = int(input("Ingresa la cantidad de calificaciones: "))

for i in range(n_calificaciones):
    calificacion = float(input(f'Ingresa la calificacion numero {i + 1}: '))
    calificaciones.append(calificacion)
print(f'\nLas calificaciones ingresadas son: {calificaciones}')

promedio = sum(calificaciones) / n_calificaciones

print(f'El promedio del estudiante es: {promedio:.2f}')