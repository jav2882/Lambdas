import tkinter as tk
from tkinter import messagebox
from RegistroCliente import RegistroCliente

class Autenticacion:
    def __init__(self, usuario_valido, password_valido):
        self.usuario_valido = usuario_valido
        self.password_valido = password_valido
        self.ventana = None
        self.entry_usuario = None
        self.entry_password = None
        self.var_recordar = None

    def iniciar_ventana(self):
        self.ventana = tk.Tk()
        self.ventana.title("Inicio de Sesion")
        self.ventana.geometry("400x350")
        self.ventana.resizable(False, False)
        
        self.ventana.bind('<Return>', lambda event: self.validar_acceso())
        
        frame_login = tk.LabelFrame(self.ventana, text="Acceso al Sistema", padx=20, pady=20)
        frame_login.pack(padx=20, pady=20, fill="both", expand=True)

        tk.Label(frame_login, text="Cual es su usuario o correo electronico").pack(anchor="w", pady=(0, 5))
        self.entry_usuario = tk.Entry(frame_login, width=40)
        self.entry_usuario.pack(pady=(0, 10))

        tk.Label(frame_login, text="Cual es su contrasena").pack(anchor="w", pady=(0, 5))
        self.entry_password = tk.Entry(frame_login, width=40, show="*")
        self.entry_password.pack(pady=(0, 10))

        self.var_recordar = tk.BooleanVar()
        tk.Checkbutton(frame_login, text="Desea recordar la sesion", variable=self.var_recordar).pack(anchor="w", pady=(0, 15))

        tk.Button(frame_login, text="Ingresar", command=lambda: self.validar_acceso(), bg="green", fg="white", width=20).pack(pady=5)
        
        tk.Button(frame_login, text="Olvido contrasena", command=lambda: self.recuperar_password(), bg="orange", fg="white", width=20).pack(pady=5)
        
        self.ventana.mainloop()

    def validar_acceso(self):
        usuario = self.entry_usuario.get()
        password = self.entry_password.get()
        
        if not usuario or not password:
            messagebox.showwarning("Validacion", "Por favor ingrese usuario y contrasena")
            return
            
        if usuario == self.usuario_valido and password == self.password_valido:
            messagebox.showinfo("Exito", "Bienvenido al sistema")
            self.ventana.destroy()
            
            ventana_registro = tk.Tk()
            app_registro = RegistroCliente(ventana_registro)
            app_registro.iniciar_ventana()
            ventana_registro.mainloop()
        else:
            messagebox.showerror("Error", "Credenciales incorrectas")

    def recuperar_password(self):
        mensaje = f"Su usuario es: {self.usuario_valido}\nSu contrasena es: {self.password_valido}"
        messagebox.showinfo("Recuperacion de Credenciales", mensaje)
