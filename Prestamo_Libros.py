print("*** Sistema Prestamo de Libros")

distancia_Km = 3
credencial = input("¿Cuentas con credencial de estudiante(Si/No)?")
distancia_biblioteca = float(input("¿A cuantos kilometros vives de la biblioteca?"))

elegible = (credencial.strip().lower() == 'si' or
            distancia_biblioteca <= distancia_Km)

print(f'Eres elegible para prestamo de libros: {elegible}')