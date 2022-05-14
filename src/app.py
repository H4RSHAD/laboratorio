from flask import Flask
from src.routes.routes import *

#Instancia del proyecto
app = Flask(__name__)

# llamar a las rutas
app.add_url_rule(routes["index_ruta"], view_func=routes["index_controller"])

app.add_url_rule(routes["delete_persona_ruta"], view_func=routes["delete_persona_controller"])
#ruta del error 404
app.register_error_handler(routes["not_found_route"], routes["not_found_controller"])
