import importlib


class Conexion:

    def __init__(self):
        self.host = "localhost"
        self.usuario = "postgres"  # Ajusta a tu usuario de PostgreSQL
        self.password = "tu_contraseña"  # Ajusta a tu contraseña
        self.base_datos = "login_mvc"
        self.puerto = "5432"

    def conectar(self):
        try:
            psycopg2 = importlib.import_module("psycopg2")
        except ImportError:
            print("Falta psycopg2. Instálalo con: pip install psycopg2-binary")
            return None

        try:
            conexion = psycopg2.connect(
                host=self.host,
                user=self.usuario,
                password=self.password,
                database=self.base_datos,
                port=self.puerto,
            )
            return conexion

        except psycopg2.Error as error:
            print("Error al conectar con PostgreSQL:", error)
            return None