print("*** Sistema Bancario ***")

salir = input("¿Deseas salir del sistema(Si/No)? ")
salir_sistema = salir.strip().lower() == 'si'

if not salir_sistema:
    print(f'Continuamos dentro del sistema')
else:
    print(f'Salimos del sistema')