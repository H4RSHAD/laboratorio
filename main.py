#Constructor del Proyecto
from src.app import app

#parametros del servidor
HOST = 'localhost'
PORT = 5500
DEBUG= True

if(__name__=='__main__'):
    app.run(HOST,PORT,DEBUG)

