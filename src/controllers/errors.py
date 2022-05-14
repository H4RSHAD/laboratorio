from flask.views import MethodView

class NoFoundController(MethodView):
    def get(self,error):
        return f"Pagina no encontrada{error}"
