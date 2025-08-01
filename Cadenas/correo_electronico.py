print("*** GENERADOR DE EMAIL ***")

#Nombre completo del usuario
nombre = " Andrés Giovanny Lagos "
print(f'Nombre usuario: {nombre}')
#Normalizar el nombre del usuario
nombre_normalizado = nombre.strip().lower().replace(' ','.')
print(f'Nombre usuario normalizado: {nombre_normalizado} ''\n')
#Nombre empresa
empresa = " Redragon Logitech "
#Normalizar el nombre de la empresa
empresa_normalizado = empresa.replace(' ','').lower()
print(f'Nombre empresa: {empresa}')
#Extension del dominio
extension_dominio = ".edu.co"
print(f'Extension del dominio: {extension_dominio}')

dominio_email = f'@{empresa_normalizado}{extension_dominio}'
print(f'Dominio de email normalizado: {dominio_email}')

#Email Final
print(f'\nEmail final generado: {nombre_normalizado}{dominio_email}')