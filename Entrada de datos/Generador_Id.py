print("*** Sistema Generador de ID unico")
from random import randint

nombre = input("Ingrese su primer nombre: ")
apellido = input("Ingrese su primer apellido: ")
anio = input("Ingrese su año de nacimiento (YYYY): ")
nombre_n = nombre.strip().upper()[0:2]
apellido_n = apellido.strip().upper()[0:2]
anio_n = anio.strip()[2:]

print(f'Hola {nombre} \n tu numero de identificacion (ID) generado por el sistema es: {nombre_n}{apellido_n}{anio_n}{randint(1000,9999)} Felicidades!')

