from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash #flash es el encargado de mostrar los mensajes

class Post:

    def __init__(self, data):
        self.id = data["id"]
        self.contenido = data["contenido"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]

        self.user_name = data["user_name"]

    @classmethod
    def save(cls, form):
        query = "INSERT INTO posts (contenido, user_id) VALUES (%(contenido)s, %(user_id)s)"
        return connectToMySQL("foro_publicaciones").query_db(query, form)
    
    @staticmethod
    def validate_post(form):
        is_valid = True

        if len(form["contenido"]) < 1:
            flash("Post content is required", "post") #("mensaje", "categoria")
            is_valid = False

        return is_valid
    
    @classmethod
    def get_all(cls):
        query = "SELECT posts.*, users.first_name as user_name FROM posts JOIN users ON posts.user_id = users.id ORDER BY created_at DESC;"
        results = connectToMySQL("foro_publicaciones").query_db(query) #results = Lista de diccionarios
        posts = []
        for p in results:
            #p = {"id":1, "contenido": Hola ....}
            posts.append(cls(p)) #1. cls(post): genera el objeto de publicacion con el diccionario.
            #2. append agrega el objeto a la lista de posts
        return posts
    
    @classmethod
    def delete(cls, data):
        #data: diccionario {} con id
        query = "DELETE FROM posts WHERE id = %(id)s"
        connectToMySQL("foro_publicaciones").query_db(query, data)
