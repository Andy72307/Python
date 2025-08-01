salir = True

while salir:
    print(f'''Menu:
    1. Suma
    2. Resta
    3. Multiplicacion
    4. Division
    5. Salir''')
    opcion = int(input("Escoje una opción: "))
    if 1 <= opcion <= 4:
        num1 = float(input("Ingresa un numero: "))
        num2 = float(input("Ingresa un segundo numero: "))
    if opcion == 1:
        suma = num1 + num2
        print(f'La suma de los numeros es {suma:.2f}\n')
    elif opcion == 2:
        resta = num1 - num2
        print(f'La resta de los numeros es {resta:.2f}\n')
    elif opcion == 3:
        mul = num1 * num2
        print(f'La multiplicacion de los numeros es {mul:.2f}\n')
    elif opcion == 4:
        div = num1 / num2
        print(f'La division de los numeros es {div:.2f}\n')
    elif opcion == 5:
        salir = False
    else:
        print('Opcion no valida\n')
else:
    print("Saliendo de la calculadora")