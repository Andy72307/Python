
salir = False
while not salir:
    print(f'''Menu:
    1. Crear Cuenta
    2. Eliminar Cuenta
    3. Salir''')
    i = int(input("Escoge una opción: "))

    if i == 1:
        print('Creando tu cuenta...\n')
    elif i == 2:
        print('Eliminando tu cuenta...\n')
    elif i == 3:
        salir = True
    else:
        print('Opcion no valida\n')
else:
    print("Fin del programa")