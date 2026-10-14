import tkinter as tk
from tkinter import ttk, messagebox

class RegistroCliente:
    def __init__(self, ventana_top):
        self.ventana = ventana_top
        
        self.var_nombre = tk.StringVar()
        self.var_tipo_doc = tk.StringVar()
        self.var_num_doc = tk.StringVar()
        self.var_fecha_nac = tk.StringVar()
        self.var_genero = tk.StringVar()
        self.var_ciudad = tk.StringVar()
        self.var_direccion = tk.StringVar()
        
        self.var_int_tecnologia = tk.BooleanVar()
        self.var_int_hogar = tk.BooleanVar()
        self.var_int_deportes = tk.BooleanVar()
        
        self.text_observaciones = None
        self.scale_satisfaccion = None

    def iniciar_ventana(self):
        self.ventana.title("Registro de Nuevos Clientes")
        self.ventana.geometry("600x800")
        
        canvas = tk.Canvas(self.ventana)
        scrollbar = ttk.Scrollbar(self.ventana, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        frame_personales = tk.LabelFrame(scrollable_frame, text="Datos Personales", padx=10, pady=10)
        frame_personales.pack(padx=20, pady=10, fill="x")

        tk.Label(frame_personales, text="Cual es el nombre completo del cliente *").grid(row=0, column=0, sticky="w", pady=2)
        tk.Entry(frame_personales, textvariable=self.var_nombre, width=40).grid(row=0, column=1, pady=2, padx=5)

        tk.Label(frame_personales, text="Cual es el tipo de documento *").grid(row=1, column=0, sticky="w", pady=2)
        combo_doc = ttk.Combobox(frame_personales, textvariable=self.var_tipo_doc, values=["CC", "CE", "Pasaporte", "NIT"])
        combo_doc.grid(row=1, column=1, sticky="w", pady=2, padx=5)

        tk.Label(frame_personales, text="Cual es el numero de documento *").grid(row=2, column=0, sticky="w", pady=2)
        tk.Entry(frame_personales, textvariable=self.var_num_doc, width=20).grid(row=2, column=1, sticky="w", pady=2, padx=5)

        tk.Label(frame_personales, text="Cual es la fecha de nacimiento (DD/MM/AAAA)").grid(row=3, column=0, sticky="w", pady=2)
        tk.Entry(frame_personales, textvariable=self.var_fecha_nac, width=15).grid(row=3, column=1, sticky="w", pady=2, padx=5)

        tk.Label(frame_personales, text="Cual es su genero").grid(row=4, column=0, sticky="w", pady=2)
        frame_genero = tk.Frame(frame_personales)
        frame_genero.grid(row=4, column=1, sticky="w")
        tk.Radiobutton(frame_genero, text="Masculino", variable=self.var_genero, value="M").pack(side="left")
        tk.Radiobutton(frame_genero, text="Femenino", variable=self.var_genero, value="F").pack(side="left")
        tk.Radiobutton(frame_genero, text="Otro", variable=self.var_genero, value="O").pack(side="left")

        frame_contacto = tk.LabelFrame(scrollable_frame, text="Contacto y Ubicacion", padx=10, pady=10)
        frame_contacto.pack(padx=20, pady=10, fill="x")

        tk.Label(frame_contacto, text="Cual es su ciudad").grid(row=0, column=0, sticky="w", pady=2)
        ciudades = ["Cucuta", "Bogota", "Medellin", "Cali", "Bucaramanga"]
        combo_ciudad = ttk.Combobox(frame_contacto, textvariable=self.var_ciudad, values=ciudades)
        combo_ciudad.grid(row=0, column=1, sticky="w", pady=2, padx=5)

        tk.Label(frame_contacto, text="Cual es su direccion").grid(row=1, column=0, sticky="w", pady=2)
        tk.Entry(frame_contacto, textvariable=self.var_direccion, width=40).grid(row=1, column=1, pady=2, padx=5)

        frame_preferencias = tk.LabelFrame(scrollable_frame, text="Preferencias y Observaciones", padx=10, pady=10)
        frame_preferencias.pack(padx=20, pady=10, fill="x")

        tk.Label(frame_preferencias, text="Cuales son sus intereses").grid(row=0, column=0, sticky="w", pady=2)
        frame_intereses = tk.Frame(frame_preferencias)
        frame_intereses.grid(row=0, column=1, sticky="w")
        tk.Checkbutton(frame_intereses, text="Tecnologia", variable=self.var_int_tecnologia).pack(side="left")
        tk.Checkbutton(frame_intereses, text="Hogar", variable=self.var_int_hogar).pack(side="left")
        tk.Checkbutton(frame_intereses, text="Deportes", variable=self.var_int_deportes).pack(side="left")

        tk.Label(frame_preferencias, text="Nivel de prioridad o satisfaccion (1-10):").grid(row=1, column=0, sticky="w", pady=10)
        self.scale_satisfaccion = tk.Scale(frame_preferencias, from_=1, to=10, orient="horizontal")
        self.scale_satisfaccion.grid(row=1, column=1, sticky="w", padx=5)

        tk.Label(frame_preferencias, text="Que observaciones adicionales desea registrar").grid(row=2, column=0, columnspan=2, sticky="w", pady=(10,0))
        self.text_observaciones = tk.Text(frame_preferencias, height=4, width=50)
        self.text_observaciones.grid(row=3, column=0, columnspan=2, pady=5)

        frame_acciones = tk.Frame(scrollable_frame, pady=20)
        frame_acciones.pack(fill="x")
        
        tk.Button(frame_acciones, text="Guardar Registro", command=lambda: self.guardar_datos(), bg="green", fg="white", width=15).pack(side="left", padx=10)
        tk.Button(frame_acciones, text="Limpiar", command=lambda: self.limpiar_campos(), bg="blue", fg="white", width=15).pack(side="left", padx=10)
        tk.Button(frame_acciones, text="Cerrar", command=lambda: self.cerrar_aplicacion(), bg="red", fg="white", width=15).pack(side="right", padx=10)

    def guardar_datos(self):
        if not self.var_nombre.get() or not self.var_tipo_doc.get() or not self.var_num_doc.get():
            messagebox.showerror("Error", "Complete los campos obligatorios (*).")
            return
            
        messagebox.showinfo("Exito", f"El cliente {self.var_nombre.get()} ha sido registrado correctamente.")
        self.cerrar_aplicacion()

    def limpiar_campos(self):
        self.var_nombre.set("")
        self.var_tipo_doc.set("")
        self.var_num_doc.set("")
        self.var_fecha_nac.set("")
        self.var_genero.set("")
        self.var_ciudad.set("")
        self.var_direccion.set("")
        self.var_int_tecnologia.set(False)
        self.var_int_hogar.set(False)
        self.var_int_deportes.set(False)
        self.scale_satisfaccion.set(1)
        self.text_observaciones.delete("1.0", "end")
        messagebox.showinfo("Limpieza", "Se han limpiado los campos del formulario.")

    def cerrar_aplicacion(self):
        self.ventana.destroy()
