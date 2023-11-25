import mysql.connector
from mysql.connector import Error


class Conexion():

    def create():
        try:
            conexion = mysql.connector.connect(
                host='54.226.201.49',
                port=3306,
                user='backend',
                password='1234',
                db='appointmenthub'
            ) 
            return conexion
        except Error as ex:
            print("Error al intentar la conexión: {0}".format(ex))
        

    