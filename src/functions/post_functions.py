import tkinter as tk
from tkinter import ttk
from datetime import datetime
from config.BDConnection import connect


def cargar_posteos(texto_posteo, id_usuario):
    try:
        connection = connect()
        if connection:
            cursor = connection.cursor()
            query = "SELECT ID_post, contenido FROM Post WHERE ID_usuario = %s"
            cursor.execute(query, (id_usuario,))
            posteos = cursor.fetchall()
            cursor.close()
            connection.close()

            # Limpiar el widget texto_posteo
            texto_posteo.delete(1.0, tk.END)

            # Mostrar los posteos en el widget texto_posteo
            for post in posteos:
                post_id, contenido = post[0], post[1]
                texto_posteo.insert(tk.END, f"{contenido}\n")

                # Agregar botón de eliminar al post
                eliminar_btn = ttk.Button(
                    texto_posteo, text="Eliminar", command=lambda post_id=post_id: eliminar_post(post_id, texto_posteo, id_usuario))
                texto_posteo.window_create(tk.END, window=eliminar_btn)
                texto_posteo.insert(tk.END, "\n")

    except Exception as e:
        print(f"Error al cargar los posteos: {str(e)}")


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

            # Agregar botón de eliminación al post
        eliminar_btn = ttk.Button(
            texto_posteo, text="Eliminar", command=lambda post_id=cursor.lastrowid: eliminar_post(post_id, texto_posteo, id_usuario))
        texto_posteo.window_create(tk.END, window=eliminar_btn)
        texto_posteo.insert(tk.END, "\n")

        # Cargar los posteos actualizados después de agregar uno nuevo
        cargar_posteos(texto_posteo, id_usuario)


# ...
def eliminar_post(post_id, texto_posteo, id_usuario):
    # Conexión a la base de datos y eliminación del post
    connection = connect()
    if connection:
        cursor = connection.cursor()
        query = "DELETE FROM Post WHERE ID_post = %s"
        cursor.execute(query, (post_id,))
        connection.commit()
        cursor.close()
        connection.close()

        # Cargar los posteos actualizados después de eliminar uno
        cargar_posteos(texto_posteo, id_usuario)  # Añade el id_usuario aquí
