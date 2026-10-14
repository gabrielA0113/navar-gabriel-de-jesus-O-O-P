import tkinter as tk
from tknter import messagebox 
from login_models import user

class LoginWindow:
    def __init__(self,root):
        self.root = root
        self.root.title("Inicio de sesion de sistema")
        self.root.geometry("400x300")
        self.root.resizable(False,False)


import tkinter as tk
from tkinter import messagebox
from Models.login_model import User
from Views.home_view import DashboardVentana

class LoginVentana:
    def __init__(self, root):
        self.root = root
        self.root.title("Acceso al Sistema")
        self.root.geometry("350x380")
        self.root.resizable(False, False)

        self._crear_interfaz()

    def _crear_interfaz(self):
        lbl_titulo = tk.Label(self.root, text="Iniciar Sesión", font=("Helvetica", 16, "bold"))
        lbl_titulo.pack(pady=25)

        lbl_usuario = tk.Label(self.root, text="Usuario:", font=("Helvetica", 10))
        lbl_usuario.pack(anchor="w", padx=30, pady=(5, 2))
        
        self.entry_usuario = tk.Entry(self.root, font=("Helvetica", 11))
        self.entry_usuario.pack(fill="x", padx=30)

        lbl_pass = tk.Label(self.root, text="Contraseña:", font=("Helvetica", 10))
        lbl_pass.pack(anchor="w", padx=30, pady=(15, 2))
        
        self.entry_pass = tk.Entry(self.root, font=("Helvetica", 11), show="*")
        self.entry_pass.pack(fill="x", padx=30)

        btn_ingresar = tk.Button(
            self.root, 
            text="Entrar", 
            font=("Helvetica", 11, "bold"),
            bg="#2196F3", 
            fg="white", 
            cursor="hand2",
            command=self._validar_login
        )
        btn_ingresar.pack(fill="x", padx=30, pady=30)

    def _validar_login(self):
        usuario_texto = self.entry_usuario.get().strip()
        pass_texto = self.entry_pass.get().strip()

        if not usuario_texto or not pass_texto:
            messagebox.showwarning("Campos Vacíos", "Por favor ingresa usuario y contraseña.")
            return

        usuario_obj = User(usuario_texto, pass_texto)
        datos_usuario = usuario_obj.auth()

        if datos_usuario and len(datos_usuario) > 0:
            usuario_encontrado = datos_usuario[0]
            nombre_usuario = usuario_encontrado.get('nombre', 'Usuario')
            
            messagebox.showinfo("Bienvenido", f"¡Hola {nombre_usuario}! Acceso concedido.")
            self._abrir_dashboard(nombre_usuario)
        else:
            messagebox.showerror("Error de Acceso", "Usuario o contraseña incorrectos.")

    def _abrir_dashboard(self, nombre_completo):
        self.root.destroy()
        root_dashboard = tk.Tk()
        DashboardVentana(root_dashboard, nombre_completo)
        root_dashboard.mainloop()

import tkinter as tk

class DashboardVentana:
    def __init__(self, root, nombre_usuario):
        self.root = root
        self.root.title("Panel Principal")
        self.root.geometry("400x250")

        lbl_mensaje = tk.Label(
            self.root, 
            text=f"¡Bienvenido/a al Sistema!\n\nUsuario activo:\n{nombre_usuario}", 
            font=("Helvetica", 12),
            justify="center"
        )
        lbl_mensaje.pack(expand=True)

from Controller.database_connection import Database_connection

class User:
    def __init__(self, username, passw):
        self.username = username
        self.password = passw 
        self.db = Database_connection()

    def auth(self):
        query = "SELECT * FROM users WHERE username = %s AND passw = %s" 
        
        result = self.db.ejecutar_consulta(query, (self.username, self.password))
        
        return result
