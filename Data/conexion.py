import mysql.connector
from mysql.connector import Error


class Conexion():

    def create():
        try:
            conexion = mysql.connector.connect(
                host='localhost',
                port=3306,
                user='root',
                password='',
                db='appointmenthub'
            ) 
        except Error as ex:
            print("Error al intentar la conexión: {0}".format(ex))
        return conexion

    