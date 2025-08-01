print("*** Sistema Autenticacion ***")
usuario = 'Lucmike0707'
contraseña = 'Andres07!!'

usuario2 = input("¿Cual es tu usuario? ")
contraseña2 = input("¿Cual es tu contraseña? ")

cuenta = usuario == usuario2 and contraseña == contraseña2

print(f'¿Tiene acceso a la cuenta? {cuenta}')