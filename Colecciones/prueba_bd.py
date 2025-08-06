import psycopg2

conexion = psycopg2.connect(user = 'postgres', password = 'Andres07', host = '127.0.0.1', port = '5432', dbname = 'tets_db')

cursor = conexion.cursor()
sentencia = 'SELECT * FROM persona'
cursor.execute(sentencia)
registros = cursor.fetchall()
print(registros)