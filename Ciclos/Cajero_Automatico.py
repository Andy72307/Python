salir = True
saldo = 1000

while salir:
    print('''Menu:
    1. Depositar
    2. Retirar
    3. Consultar saldo
    4. Salir''')
    i = int(input("Ingresa una opción: "))
    if i == 1:
        deposito = float(input("Cuanto desea depositar: "))
        saldo += deposito
        print(f'Tu nuevo saldo es de ${saldo:.2f}')
        print('')
    elif i == 2:
        retirar = float(input("Cuanto deseas retirar: "))
        if retirar > saldo:
            print(f'No cuentas con el saldo suficiente, tu saldo actual es ${saldo:.2f}')
        else:
            saldo -= retirar
            print(f'Tu nuevo saldo es ${saldo:.2f}')
        print('')
    elif i == 3:
        print(f'Tu saldo es de: ${saldo:.2f}')
        print('')
    elif i == 4:
        salir = False
    else:
        print("Opcion invalida\n")
else:
    print("Saliendo del cajero automatico")