import psycopg2  # type: ignore[reportMissingModuleSource]
from config.database import Conexion


class UserModel:

    def __init__(self):
        self.conexion_db = Conexion()

    def registrar_usuario(self, nombre, email, password):
        conexion = self.conexion_db.conectar()

        if conexion is None:
            return "error"

        cursor = None

        try:
            cursor = conexion.cursor()

            consulta = """
                INSERT INTO users (nombre, email, password)
                VALUES (%s, %s, %s)
            """

            cursor.execute(consulta, (nombre, email, password))
            conexion.commit()

            return "ok"

        except psycopg2.errors.UniqueViolation:
            conexion.rollback()
            return "duplicado"

        except psycopg2.Error as error:
            print("Error al registrar usuario:", error)
            conexion.rollback()
            return "error"

        finally:
            if cursor is not None:
                cursor.close()
            if conexion:
                conexion.close()

    def validar_usuario(self, email, password):
        conexion = self.conexion_db.conectar()

        if conexion is None:
            return None

        cursor = None

        try:
            cursor = conexion.cursor()

            consulta = """
                SELECT id, nombre
                FROM users
                WHERE email = %s AND password = %s
            """

            cursor.execute(consulta, (email, password))
            usuario = cursor.fetchone()

            return usuario

        except psycopg2.Error as error:
            print("Error al validar usuario:", error)
            return None

        finally:
            if cursor is not None:
                cursor.close()
            if conexion:
                conexion.close()

    def cerrar(self):
        pass