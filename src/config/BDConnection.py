import mysql.connector

# Configuración de la base de datos


def connect():
    try:
        connection = mysql.connector.connect(
            user='root',
            password='root',
            host='localhost',
            port='3306',
            database='AntiSocial'
        )

        return connection
    except Exception as e:
        print(f"Error al conectar a la base de datos: {str(e)}")
        return None
