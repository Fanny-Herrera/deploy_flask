#Terminal: pipenv install flask pymysql flask-bcrypt

#Importación app
from flask_app import app

#Importación controladores
from flask_app.controllers import users_controller, posts_controller

#Ejecución app
if __name__ == "__main__":
    app.run(debug = True)