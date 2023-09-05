#Importamos conector
import mysql.connector

#creamos la conexion
conexion = mysql.connector.connect(user='root', 
                                   password='root',
                                   host='localhost',
                                   port='3306',
                                   database= "northwind")

cursor = conexion.cursor()

#Muestra bases de datos existentes
"""cursor.execute("SHOW DATABASES")

 for bd in cursor: 
    print(bd)"""
#Crea una base de datos nueva
# cursor.execute("CREATE DATABASE desdePy")

#Ejecutar la consulta
cursor.execute("SELECT * FROM shippers;")


# Insertar datos en una tabla
""" query_insertar = "INSERT INTO shippers (ShipperID, ShipperName,Phone) VALUES (%s, %s, %s)"
data = (4, "OCASA", "362-1234")
cursor.execute(query_insertar, data)

#Mandar la instruccion
conexion.commit() """


# Borrar datos de una tabla
'''query_borrar = "DELETE FROM shippers WHERE ShipperID = 4"
cursor.execute(query_borrar)

#Mandar la instruccion
conexion.commit() '''

#Obtener todos los datos y mostrarlos
resultado = cursor.fetchall()

for registro in resultado:
    print(registro)
    

# print(conexion) 

cursor.close()
conexion.close()