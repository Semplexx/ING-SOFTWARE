import customtkinter as ctk
from tkinter import messagebox
import main

class NominaInterface:
    def __init__(self, master):
        self.root = ctk.CTk()
        self.root.title("Nómina")
        self.root.geometry("400x300")

        ctk.CTkLabel(self.root, text="Bienvenido a Nómina", font=("Arial", 18)).pack(pady=20)
        ctk.CTkButton(self.root, text="Cerrar sesión", command=self.cerrar_sesion).pack(pady=10)

        self.root.mainloop()

    def cerrar_sesion(self):
        self.root.destroy()
        main.Main()