from random import randint
print("*** Sistema Generador de Emails ***")
nombre = input("Ingrese sus nombres: ")
apellido = input("Ingrese sus apellidos: ")
nombre_empresa = input("Ingrese el nombre de su empresa: ")
dominio = input("Ingrese la extension de dominio: ")
nombre_completo = (f'{nombre} {apellido}')
nombre_completon = nombre_completo.strip().lower().replace(' ','.')
nombre_empresan = nombre_empresa.strip().lower().replace(' ','')
dominio_n = dominio.strip().lower().replace(' ','')
email = (f'{nombre_completon}@{nombre_empresan}{dominio_n}')
email_completo = f'''
Tu email queda de la siguiente manera: 
    {email}'''
print(email_completo)

