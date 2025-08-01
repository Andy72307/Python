#Revisar si una variable se encuentra dentro de rango 1 y 10
dato = int(input("Introduce un dato entero: "))

#Revisamos si esta dentro de rango
# rango = 1 <= dato <= 10
# print(f'¿Variable esta dentro de rango (1 y 10)?: {rango}')

#Revisamos la logica inversa para saber si el dato esta fuera de rango
rango = not(1 <= dato <= 10)
print(f'¿Variable esta fuera de rango (entre 1 y 10)? {rango}')