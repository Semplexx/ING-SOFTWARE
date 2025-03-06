import customtkinter as ctk
from tkinter import ttk, messagebox
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from conexion import Conexion

class NominaInterface:
    def __init__(self, root):
        self.root = root
        self.window = ctk.CTkToplevel(root)
        self.window.title("Gestión de Nómina")
        self.window.geometry("700x400")

        self.conn = Conexion.conexionBaseDeDatos()
        self.setup_ui()
        self.cargar_empleados()

    def setup_ui(self):
        # Tabla de empleados
        self.tree = ttk.Treeview(self.window, columns=("ID", "Nombre", "Apellido", "Cédula", "Correo"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Apellido", text="Apellido")
        self.tree.heading("Cédula", text="Cédula")
        self.tree.heading("Correo", text="Correo")
        
        self.tree.column("ID", width=50)
        self.tree.column("Nombre", width=150)
        self.tree.column("Apellido", width=150)
        self.tree.column("Cédula", width=100)
        self.tree.column("Correo", width=200)

        self.tree.bind("<Double-1>", self.ver_detalle_empleado)
        self.tree.pack(pady=10, padx=10, fill="both", expand=True)

        # Botones
        btn_frame = ctk.CTkFrame(self.window)
        btn_frame.pack(pady=10)
        
        self.btn_agregar = ctk.CTkButton(btn_frame, text="Agregar Empleado", command=self.agregar_empleado)
        self.btn_agregar.grid(row=0, column=0, padx=5)
        
        self.btn_editar = ctk.CTkButton(btn_frame, text="Editar Empleado", command=self.editar_empleado)
        self.btn_editar.grid(row=0, column=1, padx=5)
        
        self.btn_eliminar = ctk.CTkButton(btn_frame, text="Eliminar Empleado", command=self.eliminar_empleado)
        self.btn_eliminar.grid(row=0, column=2, padx=5)

    def cargar_empleados(self):
        if self.conn:
            cursor = self.conn.cursor()
            query = "SELECT id_empleado, nombre, apellido, numero_documento, correo FROM empleados"
            cursor.execute(query)
            empleados = cursor.fetchall()
            cursor.close()

            self.tree.delete(*self.tree.get_children())
            for emp in empleados:
                self.tree.insert("", "end", values=emp)

    def ver_detalle_empleado(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            empleado = self.tree.item(selected_item, "values")
            messagebox.showinfo("Detalles del Empleado", f"ID: {empleado[0]}\nNombre: {empleado[1]}\nApellido: {empleado[2]}\nCédula: {empleado[3]}\nCorreo: {empleado[4]}")

    def agregar_empleado(self):
        messagebox.showinfo("Agregar", "Aquí se abriría el formulario para agregar un empleado.")

    def editar_empleado(self):
        messagebox.showinfo("Editar", "Aquí se abriría el formulario para editar un empleado seleccionado.")

    def eliminar_empleado(self):
        selected_item = self.tree.selection()
        if selected_item:
            empleado = self.tree.item(selected_item, "values")
            confirmar = messagebox.askyesno("Eliminar", f"¿Seguro que deseas eliminar a {empleado[1]} {empleado[2]}?")
            if confirmar:
                cursor = self.conn.cursor()
                query = "DELETE FROM empleados WHERE id = %s"
                cursor.execute(query, (empleado[0],))
                self.conn.commit()
                cursor.close()
                self.cargar_empleados()
        else:
            messagebox.showwarning("Eliminar", "Selecciona un empleado para eliminar.")
