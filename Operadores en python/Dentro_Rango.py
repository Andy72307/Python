print("*** Valor Dentro de Rango ***")
valor_minimo, valor_maximo = 0, 5
numero = float(input(f"Ingrese un numero entre {valor_minimo} y {valor_maximo}: "))
comprobacion = valor_minimo <= numero <= valor_maximo


print(f'¿El numero esta dentro del rango? {comprobacion}')