print("*** Casa de los Espejos ***")
edad = int(input("Ingrese su edad: "))
miedo = input("¿Tienes miedo a la oscuridad(Si/No)? ")
miedo = miedo.strip().lower() == 'si'

if edad >= 10 and not miedo:
    print(f'Puede entrar tiene {edad} años y no le tiene miedo a la oscuridad')
else:
    print(f'No puede entrar puede darle miedo')