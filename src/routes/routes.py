#Todas las rutas
from src.controllers.controller import *
from src.controllers.errors import NoFoundController

#diccionario de todas las rutas

routes = {
    "index_ruta": "/","index_controller":Index.as_view("index"),  #Inicio
    "delete_persona_ruta":"/eliminar/persona<int:ci>","delete_persona_controller": DeletePersonaController.as_view("delete_persona"),
    "not_found_route":404,"not_found_controller": NoFoundController.as_view("Not_found")
}