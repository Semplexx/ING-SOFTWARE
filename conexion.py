import mysql.connector

class Conexion:
    @staticmethod
    def conexionBaseDeDatos():
        try:
            conexion = mysql.connector.connect(
                user='root',
                password='',  # Ajusta según tu configuración
                host='127.0.0.1',
                database='login',
                port='3306'
            )
            return conexion
        except mysql.connector.Error as error:
            raise Exception(f"Error al conectarse a la base de datos: {error}")

    @staticmethod
    def cerrarConexion(conexion):
        """Cierra la conexión a la base de datos si está activa"""
        if conexion and conexion.is_connected():
            conexion.close()
            print("Conexión cerrada")