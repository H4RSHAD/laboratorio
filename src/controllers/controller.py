# Los controladores
from flask import request,render_template, redirect
from flask.views import MethodView      #para las vistas 
from src.db import connection           #para la conexion con la db.py

class Index(MethodView):
    def get(self):
        # para realizar vistas(mostrar) de los datos de la base de datos GET
        with connection.cursor() as cur:
            cur.execute("SELECT * FROM Persona")
            data = cur.fetchall()
            return render_template('public/index.html', data=data)
    
    def post(self):
        # para realizar REGISTRO en la base de datos POST
        ci = request.form['CI']
        nombre = request.form['Nombre']
        apellidoP = request.form['ApellidoP']
        apellidoM = request.form['ApellidoM']
        telefono = request.form['Telefono']
        correo = request.form['Correo']
        fecha_Nacimiento = request.form['Fecha_Nacimiento']

        #Insertando datos en la base de datos
        #print(ci,nombre,apellidoP,apellidoM,telefono,correo,fecha_Nacimiento)
        #table Persona
        with connection.cursor() as cur:
            cur.execute("INSERT INTO Persona VALUES(%s,%s,%s,%s,%s,%s,%s)",(ci,nombre,apellidoP,apellidoM,telefono,correo,fecha_Nacimiento))
            cur.connection.commit()
        return redirect('/')

class DeletePersonaController(MethodView):
    # PARA ELIMINAR de la tabla Persona de la base de datos
    def post(self,CI):
        return f"Persona {CI}" 
