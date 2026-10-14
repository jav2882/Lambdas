import tkinter as tk
from tkinter import messagebox
from Autenticacion import Autenticacion

class CrearCuenta:
    def __init__(self):
        self.ventana = None
        self.entry_usuario = None
        self.entry_password = None

    def iniciar_ventana(self):
        self.ventana = tk.Tk()
        self.ventana.title("Crear Cuenta del Sistema")
        self.ventana.geometry("400x250")
        self.ventana.resizable(False, False)

        frame = tk.LabelFrame(self.ventana, text="Configurar Nueva Cuenta", padx=20, pady=20)
        frame.pack(padx=20, pady=20, fill="both", expand=True)

        tk.Label(frame, text="Nuevo Usuario:").pack(anchor="w", pady=(0, 5))
        self.entry_usuario = tk.Entry(frame, width=40)
        self.entry_usuario.pack(pady=(0, 10))

        tk.Label(frame, text="Nueva Contrasena:").pack(anchor="w", pady=(0, 5))
        self.entry_password = tk.Entry(frame, width=40, show="*")
        self.entry_password.pack(pady=(0, 15))

        tk.Button(frame, text="Crear y Continuar", command=self.crear_cuenta, bg="blue", fg="white", width=20).pack()
        self.ventana.mainloop()

    def crear_cuenta(self):
        usuario = self.entry_usuario.get()
        password = self.entry_password.get()
        
        if not usuario or not password:
            messagebox.showwarning("Alerta", "Todos los campos son obligatorios")
            return
        
        self.ventana.destroy()
        
        app_login = Autenticacion(usuario, password)
        app_login.iniciar_ventana()
