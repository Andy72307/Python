print('*** Alcance de variables ***')

# Variable global
contador_global = 0

def incrementarContador():
    # Declarar una variable local
    contador_local = 0

    # Usar la variable global
    global contador_global 
    contador_global += 1

    # Incrementar la variable local
    contador_local += 1

    # Imprimir ambos contadores 
    print(f'Contador local: {contador_local}')
    print(f'Contador local: {contador_global}\n')

# Llamar varias veces la funcion 
incrementarContador()
