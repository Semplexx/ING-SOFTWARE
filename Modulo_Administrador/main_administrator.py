import customtkinter as ctk 
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from nomina import NominaInterface

class AdministratorInterface:
    def __init__(self, root=None):
        self.root = root if root else ctk.CTk()
        self.root.title("Administrador")
        self.root.geometry("400x400")

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure([0, 1], weight=1)

        self.btn_nomina = ctk.CTkButton(self.root, text="Nómina", command=self.abrir_nomina)
        self.btn_nomina.grid(row=0, column=0, pady=20, padx=50, sticky="ew")  # Cambiar pack() por grid()

        self.btn_inventario = ctk.CTkButton(self.root, text="Inventario", command=self.abrir_inventario)
        self.btn_inventario.grid(row=1, column=0, pady=10, padx=50, sticky="ew")  # Cambiar pack() por grid()

        if not root:
            self.root.mainloop()


    # Función para abrir la interfaz de Nómina
    def abrir_nomina(self):
        self.root.withdraw()  # Ocultar la ventana actual
        NominaInterface(self.root)  # Llamar a la interfaz de Nómina

    # Función para abrir la interfaz de Inventario
    def abrir_inventario(self):
        print("Abrir Inventario")  # Aquí puedes abrir otra ventana

# Ejecutar la interfaz si el script es ejecutado directamente
if __name__ == "__main__":
    AdministratorInterface()
