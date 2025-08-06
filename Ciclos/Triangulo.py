
n_filas = int(input("Ingresa la cantidad de filas: "))


for i in range(1, n_filas + 1):
    espacios = ' ' * (n_filas - i)
    asterisco = '*' * (2 * i - 1)
    print(espacios, asterisco)
