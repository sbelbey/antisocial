import mysql.connector


class Database:
    def __init__(self):
        connection = mysql.connector.connect(
            user='root',
            password='root',
            host='localhost',
            port='3306',
            database='RedSocial'
        )
        self.cursor = self.connection.cursor()
