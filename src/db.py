# Conectando con Posgres
import psycopg2

try:
    connection = psycopg2.connect(
        host = 'localhost',
        user = 'postgres',
        password = 'root',
        database = 'BD_Lab'
    )
    print('Conexion con la base de datos "Exitosa"')
    '''
    esto es para realizar una prueba, comentarlo para que no haga consultas cada vez que se llame 
    cursor = connection.cursor()
    cursor.execute("SELECT version() ")
    row = cursor.fetchone()
    print(row)

    cursor.execute("SELECT * FROM Persona")
    rows = cursor.fetchall() 
    for row in rows:
        print(row)
    '''
except Exception as ex:
    print(ex)
    
finally:
    print("Conexión finalizada")