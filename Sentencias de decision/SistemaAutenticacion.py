usuario_C = 'andreslagos'
password_C = 'HolaMundo123'

usuario = input("Nombre de usuario: ")
password = input("Contraseña: ")

if usuario == usuario_C and password == password_C:
    print(f'Bienvenido al sistema')
elif usuario == usuario_C:
    print(f'Contraseña no valida')
elif password_C == password:
    print(f'Usuario no valido')
else:
    print(f'Usuario y Contraseña invalidos')