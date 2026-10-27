import psycopg2  # type: ignore[reportMissingModuleSource]
import tkinter as tk


class Conexion:

    def __init__(self):
        self.host = "localhost"
        self.usuario = "postgres"  # Ajusta a tu usuario de PostgreSQL
        self.password = "tu_contraseña"  # Ajusta a tu contraseña
        self.base_datos = "login_mvc"
        self.puerto = "5432"

    def conectar(self):
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
        import psycopg2
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
from tkinter import messagebox


class LoginView:

    def __init__(self, root):
        self.root = root

        # Configuración de ventana
        self.root.title("Sistema de acceso")
        self.root.geometry("420x350")
        self.root.configure(bg="#EAF2F8")
        self.root.resizable(False, False)

        # Encabezado
        self.titulo = tk.Label(
            root,
            text="INICIAR SESIÓN",
            font=("Arial", 20, "bold"),
            bg="#EAF2F8",
            fg="#154360",
        )
        self.titulo.pack(pady=20)

        # Correo electrónico
        self.lbl_email = tk.Label(
            root, text="Correo electrónico:", font=("Arial", 11), bg="#EAF2F8"
        )
        self.lbl_email.pack()

        self.entry_email = tk.Entry(root, width=35, font=("Arial", 11))
        self.entry_email.pack(pady=5)

        # Contraseña
        self.lbl_password = tk.Label(
            root, text="Contraseña:", font=("Arial", 11), bg="#EAF2F8"
        )
        self.lbl_password.pack()

        self.entry_password = tk.Entry(
            root, width=35, font=("Arial", 11), show="*"
        )
        self.entry_password.pack(pady=5)

        # Botones
        self.btn_login = tk.Button(
            root,
            text="Ingresar",
            width=20,
            bg="#2874A6",
            fg="white",
            font=("Arial", 11, "bold"),
            cursor="hand2",
        )
        self.btn_login.pack(pady=15)

        self.btn_register = tk.Button(
            root,
            text="Crear cuenta",
            width=20,
            bg="#27AE60",
            fg="white",
            font=("Arial", 10),
            cursor="hand2",
        )
        self.btn_register.pack()

    def obtener_datos(self):
        email = self.entry_email.get().strip()
        password = self.entry_password.get()
        return email, password

    def limpiar_campos(self):
        self.entry_email.delete(0, tk.END)
        self.entry_password.delete(0, tk.END)

    def mostrar_mensaje(self, titulo, mensaje, tipo="info"):
        if tipo == "error":
            messagebox.showerror(titulo, mensaje, parent=self.root)
        else:
            messagebox.showinfo(titulo, mensaje, parent=self.root)

            import tkinter as tk
from tkinter import messagebox


class RegisterView:

    def __init__(self, root):
        self.ventana = tk.Toplevel(root)

        # Configuración de ventana emergente
        self.ventana.title("Registro de usuarios")
        self.ventana.geometry("420x440")
        self.ventana.configure(bg="#E8F8F5")
        self.ventana.resizable(False, False)

        # Bloquea la interacción con la ventana principal mientras esta exista
        self.ventana.transient(root)
        self.ventana.grab_set()

        # Encabezado
        self.titulo = tk.Label(
            self.ventana,
            text="CREAR CUENTA",
            font=("Arial", 19, "bold"),
            bg="#E8F8F5",
            fg="#117864",
        )
        self.titulo.pack(pady=18)

        # Nombre
        self.lbl_nombre = tk.Label(
            self.ventana,
            text="Nombre completo:",
            bg="#E8F8F5",
            font=("Arial", 10),
        )
        self.lbl_nombre.pack()

        self.entry_nombre = tk.Entry(self.ventana, width=35, font=("Arial", 10))
        self.entry_nombre.pack(pady=4)

        # Email
        self.lbl_email = tk.Label(
            self.ventana,
            text="Correo electrónico:",
            bg="#E8F8F5",
            font=("Arial", 10),
        )
        self.lbl_email.pack()

        self.entry_email = tk.Entry(self.ventana, width=35, font=("Arial", 10))
        self.entry_email.pack(pady=4)

        # Contraseña
        self.lbl_password = tk.Label(
            self.ventana, text="Contraseña:", bg="#E8F8F5", font=("Arial", 10)
        )
        self.lbl_password.pack()

        self.entry_password = tk.Entry(
            self.ventana, width=35, show="*", font=("Arial", 10)
        )
        self.entry_password.pack(pady=4)

        # Confirmación de contraseña
        self.lbl_confirmar = tk.Label(
            self.ventana,
            text="Confirmar contraseña:",
            bg="#E8F8F5",
            font=("Arial", 10),
        )
        self.lbl_confirmar.pack()

        self.entry_confirmar = tk.Entry(
            self.ventana, width=35, show="*", font=("Arial", 10)
        )
        self.entry_confirmar.pack(pady=4)

        # Botones
        self.btn_guardar = tk.Button(
            self.ventana,
            text="Registrar usuario",
            width=22,
            bg="#17A589",
            fg="white",
            font=("Arial", 10, "bold"),
            cursor="hand2",
        )
        self.btn_guardar.pack(pady=12)

        self.btn_cancelar = tk.Button(
            self.ventana,
            text="Cancelar",
            width=22,
            command=self.cerrar,
            cursor="hand2",
        )
        self.btn_cancelar.pack()

        self.entry_nombre.focus_set()

    def obtener_datos(self):
        nombre = self.entry_nombre.get().strip()
        email = self.entry_email.get().strip()
        password = self.entry_password.get()
        confirmar = self.entry_confirmar.get()
        return nombre, email, password, confirmar

    def mostrar_mensaje(self, titulo, mensaje, tipo="info"):
        if tipo == "error":
            messagebox.showerror(titulo, mensaje, parent=self.ventana)
        else:
            messagebox.showinfo(titulo, mensaje, parent=self.ventana)

    def cerrar(self):
        self.ventana.destroy()

        import tkinter as tk
class Authentication:

    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista
        self.vista_registro = None

        # Asignar funciones a los botones de la vista principal
        self.vista.btn_login.config(command=self.iniciar_sesion)
        self.vista.btn_register.config(command=self.abrir_registro)

        # Evento para cerrar aplicación
        self.vista.root.protocol("WM_DELETE_WINDOW", self.cerrar_aplicacion)

    def iniciar_sesion(self):
        email, password = self.vista.obtener_datos()

        if not email or not password:
            self.vista.mostrar_mensaje(
                "Campos vacíos", "Ingresa el correo y la contraseña.", "error"
            )
            return

        usuario = self.modelo.validar_usuario(email, password)

        if usuario is not None:
            id_usuario, nombre = usuario
            self.vista.mostrar_mensaje(
                "Acceso correcto", f"Bienvenido, {nombre}."
            )
            self.vista.limpiar_campos()
        else:
            self.vista.mostrar_mensaje(
                "Acceso denegado", "Correo o contraseña incorrectos.", "error"
            )

    def abrir_registro(self):
        # Evitar abrir múltiples ventanas de registro al mismo tiempo
        if (
            self.vista_registro is not None
            and self.vista_registro.ventana.winfo_exists()
        ):
            self.vista_registro.ventana.lift()
            self.vista_registro.ventana.focus_force()
            return

        self.vista_registro = RegisterView(self.vista.root)
        self.vista_registro.btn_guardar.config(command=self.registrar_usuario)
        self.vista_registro.ventana.protocol(
            "WM_DELETE_WINDOW", self.cerrar_registro
        )

    def registrar_usuario(self):
        nombre, email, password, confirmar = self.vista_registro.obtener_datos()

        if not nombre or not email or not password or not confirmar:
            self.vista_registro.mostrar_mensaje(
                "Campos vacíos", "Todos los campos son obligatorios.", "error"
            )
            return

        if "@" not in email or "." not in email.split("@")[-1]:
            self.vista_registro.mostrar_mensaje(
                "Correo inválido",
                "Ingresa un correo electrónico válido.",
                "error",
            )
            return

        if password != confirmar:
            self.vista_registro.mostrar_mensaje(
                "Contraseñas diferentes",
                "Las contraseñas no coinciden.",
                "error",
            )
            return

        resultado = self.modelo.registrar_usuario(nombre, email, password)

        if resultado == "ok":
            self.vista_registro.mostrar_mensaje(
                "Registro exitoso", "El usuario se registró correctamente."
            )
            self.cerrar_registro()
            self.vista.entry_email.delete(0, tk.END)
            self.vista.entry_email.insert(0, email)

        elif resultado == "duplicado":
            self.vista_registro.mostrar_mensaje(
                "Correo existente",
                "Ya existe una cuenta con ese correo.",
                "error",
            )
        else:
            self.vista_registro.mostrar_mensaje(
                "Error",
                "No fue posible registrar el usuario. Verifica la conexión con PostgreSQL.",
                "error",
            )

    def cerrar_registro(self):
        if self.vista_registro is not None:
            if self.vista_registro.ventana.winfo_exists():
                self.vista_registro.cerrar()
            self.vista_registro = None

    def cerrar_aplicacion(self):
        self.cerrar_registro()
        self.modelo.cerrar()
        self.vista.root.destroy()