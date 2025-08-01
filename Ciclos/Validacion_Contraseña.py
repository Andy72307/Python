contra = input("Ingresa una contraseña (Debe de tener al menos 6 caracteres): ")

while len(contra) < 6:
    print("La contraseña no cumple con los requisitos debe de tener almenos 6 caracteres")
    contra = input("Ingresa una nueva contraseña: ")
else:
    print(f'Tu contraseña se creo correctamente {contra}')