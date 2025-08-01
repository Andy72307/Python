i = 1
numero = 5
suma = 0

while i <= numero:
    print(f'(suma + i) -> {suma} + {i}')

    suma += i
    i += 1

    print(f'Suma parcial acumulada: {suma}\n')

print(f'\nResultado de al suma: {suma}')