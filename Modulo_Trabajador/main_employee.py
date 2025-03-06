import customtkinter as ctk
from tkinter import messagebox

class InventarioInterface:
    def __init__(self, master):
        self.root = ctk.CTk()
        self.root.title("Inventario")
        self.root.geometry("400x300")

        ctk.CTkLabel(self.root, text="Bienvenido a Inventario", font=("Arial", 18)).pack(pady=20)
        ctk.CTkButton(self.root, text="Salir", command=self.cerrar_sesion).pack(pady=10)

        self.root.mainloop()

    def cerrar_sesion(self):
        self.root.destroy()
        self.Main()