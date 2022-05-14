# Proyecto laboratorio Clinico
**Proyecto de la materia de Sistema de Información 1**
1. [Uso de pip para instalar requerimientos](#run)


# Version de python 
Python 3.10.4

## <a name='run'>Uso de pip para instalar requerimientos</a>

1. Abre una terminal de comandos
2. Navega hasta la raíz del proyecto donde quieres listar las dependencias
3. Ejecuta

```python
pip freeze > requirements.txt
```

4. Abre el archivo requirements.txt creado, este listará todas las dependecias de paquetes así como la versión del mismo que tu proyecto requiere para funcionar:

Para instalar esta lista de dependencias en cualquier otra instalación de Python puedes ejecutar

```python
pip install -r requirements.txt
