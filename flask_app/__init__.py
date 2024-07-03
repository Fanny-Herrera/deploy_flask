from flask import Flask #importación de flask

app = Flask(__name__) #inicialización de la app

app.secret_key = "Llave secretisima"; #Necesaria para la sesión
