import mysql.connector

from mysql.connector import Error, MySQLConnection


def crear_conexion_pool(host: str, bd: str, usuario: str, contrasena: str)-> MySQLConnection:
    try:
        conexion = mysql.connector.pooling.MySQLConnectionPool(
            pool_name=bd,
            user=usuario,
            password=contrasena,
            host=host,
            database=bd
        )
        if conexion.is_connected():
            return conexion
        else:
            print("No se logró conectar a la base de datos")
            raise Exception("Error al conectar a la base de datos")
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        raise


def cerrar_conexion(conexion: MySQLConnection):
    try:
        if conexion.is_connected():
            conexion.close()
    except Exception as e:
        print(f"Error al cerrar la conexión: {e}")
