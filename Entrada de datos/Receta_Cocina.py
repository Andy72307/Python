print("*** Receta de Cocina ***")

nombre = input("Ingrese el nombre de la receta: ")
ingredientes = input("Ingrese los ingredientes necesarios para esta receta: ")
tiempo = int(input("Ingrese el tiempo necesario para preparar esta receta (en minutos): "))
dificultad = input("Ingrese la dificultad de la receta (Fácil, Media, Alta): ")
print("----------------")

print(f'Nombre de la receta: {nombre}')
print(f'Ingredientes: {ingredientes}')
print(f'Tiempo de preparación: {tiempo}')
print(f'Dicifultad: {dificultad}')