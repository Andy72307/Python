from random import randint
intento_max = 5
intento = 0
numero = randint(1, 50)
print(f"El numero maximo de intentos es de {intento_max}\n")
numero2 = None
while numero2 != numero and intento < intento_max:
    numero2 = int(input("Adivina el numero secreto: "))
    if numero2 < numero:
        print("EL numero secreto es mayor")
    elif numero2 > numero:
        print("El numero secreto es menor")
    intento += 1
if numero2 == numero:
    print(f'Felicidades adivinaste el numero en {intento} intentos')
else:
    print(f'Agotaste tu numero de intentos el numero secreto era {numero}')