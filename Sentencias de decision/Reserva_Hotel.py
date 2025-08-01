print('*** Sistema de Reserva de Hotel ***')

#Constantes
si_cuarto = 190.50
no_cuarto = 150.50
#Variables
nombre = input("Nombre del Cliente: ")
dias = int(input("Días de estadía: "))
cuarto = input("¿Con vista al mar (Si/No)? ")
cuarto = cuarto.strip().lower() == 'si'

if cuarto:
    costo = si_cuarto * dias
else:
    costo = no_cuarto * dias

print("-------------Detalles de la Reservación-------------")
print(f'''Cliente: {nombre}
Dias de estadía: {dias}
Costo total: ${costo:.2f}
Habitación con vista al mar: {'Si' if cuarto else 'No'}''')