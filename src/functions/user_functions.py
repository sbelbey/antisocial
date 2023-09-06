from config.BDConnection import connect


def obtener_datos_usuario(id_usuario):
    try:
        connection = connect()
        if connection:
            cursor = connection.cursor()
            query = "SELECT nombre_usuario, nombre, apellido FROM Usuario WHERE ID_usuario = %s"
            cursor.execute(query, (id_usuario,))
            resultado = cursor.fetchone()
            cursor.close()
            connection.close()
            # Devuelve una tupla (nombre_usuario, nombre, apellido)
            return resultado
    except Exception as e:
        print(f"Error al obtener datos del usuario: {str(e)}")
    return None
