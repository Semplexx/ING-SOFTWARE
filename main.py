from tkinter import messagebox
import customtkinter as ctk
from conexion import Conexion
from Modulo_Nomina import main_nomina
from Modulo_Inventario import main_inventario

class Main:
    def __init__(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        try:
            self.conn = Conexion.conexionBaseDeDatos()
        except Exception as e:
            messagebox.showerror("Error de conexión", str(e))
            return  # No inicia la GUI si hay error

        self.root = ctk.CTk()
        self.root.title("Login")
        self.root.geometry("400x300")

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure([0, 1, 2, 3, 4], weight=1)

        ctk.CTkLabel(self.root, text="Iniciar sesión", font=("Arial", 20)).grid(row=0, column=0, pady=10)

        self.entry_user = ctk.CTkEntry(self.root, placeholder_text="Usuario")
        self.entry_user.grid(row=1, column=0, pady=5, padx=50, sticky="ew")

        self.entry_password = ctk.CTkEntry(self.root, placeholder_text="Contraseña", show="*")
        self.entry_password.grid(row=2, column=0, pady=5, padx=50, sticky="ew")

        self.boton_login = ctk.CTkButton(self.root, text="Ingresar", command=self.verify_login)
        self.boton_login.grid(row=3, column=0, pady=20, padx=50, sticky="ew")

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def verify_login(self):
        user = self.entry_user.get()
        password = self.entry_password.get()

        if self.conn:
            cursor = self.conn.cursor()
            query = "SELECT tipo_usuario FROM usuarios WHERE usuario = %s AND contraseña = %s"
            cursor.execute(query, (user, password))
            result = cursor.fetchone()

            if result:
                tipo_usuario = result[0]
                if tipo_usuario == "NOMINA":
                    self.abrir_nomina()
                elif tipo_usuario == "INVENTARIO":
                    self.abrir_inventario()
                else:
                    messagebox.showerror("Error", "Tipo de usuario no reconocido")
            else:
                messagebox.showerror("Error", "Usuario o contraseña incorrectos")

            cursor.close()
        else:
            messagebox.showerror("Error", "No hay conexión a la base de datos")

    def abrir_nomina(self):
        self.root.withdraw()
        main_nomina.NominaInterface(self.root)

    def abrir_inventario(self):
        self.root.withdraw()
        main_inventario.InventarioInterface(self.root)

    def on_closing(self):
        """Cerrar conexión al salir"""
        if self.conn:
            Conexion.cerrarConexion(self.conn)
        self.root.destroy()

if __name__ == "__main__":
    app = Main()
