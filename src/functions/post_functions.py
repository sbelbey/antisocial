import tkinter as tk
from datetime import datetime
from config.BDConnection import connect


def crear_post(entry_post, texto_posteo, id_usuario):
    contenido = entry_post.get()
    if contenido:
        tiempo_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        texto_post = f"[{tiempo_actual}] {contenido}\n"
        texto_posteo.insert(tk.END, texto_post)
        entry_post.delete(0, tk.END)

        # Conexión a la base de datos y creación del post
        connection = connect()
        if connection:
            cursor = connection.cursor()
            query = "INSERT INTO Post (ID_usuario, contenido, timestamp) VALUES (%s, %s, NOW())"
            values = (id_usuario, contenido)
            cursor.execute(query, values)
            connection.commit()
            cursor.close()
            connection.close()
