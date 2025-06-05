import tkinter as tk
from tkinter import ttk, messagebox

from controladores.comunicacion import Comunicacion
from modelos.autor import Autor
from modelos.libro import Libro
from .tabla import Tabla  

class BibliotecaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Biblioteca")
        self.root.geometry("1200x700") 
        self.root.resizable(False, False)

        self.comunicacion = Comunicacion()

        self.autor = Autor(root)
        self.libro = Libro(root)

        self.tab_control = ttk.Notebook(self.root)
        self.autor_tab = tk.Frame(self.tab_control, bg="#D6EAF8")
        self.libro_tab = tk.Frame(self.tab_control, bg="#D6EAF8")
        self.tab_control.add(self.autor_tab, text="AUTOR")
        self.tab_control.add(self.libro_tab, text="LIBRO")
        self.tab_control.pack(expand=1, fill="both")

        self.crear_ventana_autor()
        self.crear_ventana_libro()

    #  AUTORES 
    def crear_ventana_autor(self):
        tk.Label(self.autor_tab, text="AUTOR", font=("Arial", 22), bg="#D6EAF8").pack(pady=10)
        frame = tk.LabelFrame(self.autor_tab, text="Datos de autor", padx=10, pady=10, bg="#D6EAF8")
        frame.place(x=20, y=60, width=300, height=200)

        campos = [("ID", self.autor.id), ("Nombre", self.autor.nombre),
                  ("Nacionalidad", self.autor.nacionalidad), ("Edad", self.autor.edad)]

        for i, (etiqueta, variable) in enumerate(campos):
            tk.Label(frame, text=f"{etiqueta}:", anchor="w", bg="#D6EAF8").grid(row=i, column=0, sticky="w", pady=2)
            tk.Entry(frame, width=25, textvariable=variable).grid(row=i, column=1, pady=2)

        btn_frame = tk.Frame(self.autor_tab, bg="#D6EAF8")
        btn_frame.place(x=20, y=280)
        botones = ["Enviar", "Consultar", "Actualizar", "Eliminar", "Limpiar", "Consultar Todos"]
        funciones = [self.guardar_autor, self.consultar_autor, self.actualizar_autor,
                     self.eliminar_autor, self.limpiar_autor, self.consultar_todos_autores]
        for i, (texto, funcion) in enumerate(zip(botones, funciones)):
            tk.Button(btn_frame, text=texto, width=15, command=funcion).grid(row=i // 2, column=i % 2, padx=5, pady=3)

        columnas = ["ID", "NOMBRE", "NACIONALIDAD", "EDAD"]
        self.tabla_autores = Tabla(self.autor_tab, columnas, columnas, [])
        self.tabla_autores.tabla.place(x=350, y=60, width=800, height=550)

    def guardar_autor(self):
        try:
            self.comunicacion.guardar_autor(self.autor.nombre.get(), self.autor.nacionalidad.get(), int(self.autor.edad.get()))
            messagebox.showinfo("Éxito", "Autor guardado correctamente")
            self.consultar_todos_autores()
        except Exception as e:
            messagebox.showerror("Error", f"Datos inválidos: {e}")

    def consultar_autor(self):
        id_ = self.autor.id.get()
        if not id_:
            return messagebox.showwarning("Aviso", "Ingrese un ID")
        autor = self.comunicacion.consultar_autor(id_)
        if autor:
            self.autor.id.set(autor['id'])
            self.autor.nombre.set(autor['nombre'])
            self.autor.nacionalidad.set(autor['nacionalidad'])
            self.autor.edad.set(autor['edad'])
        else:
            messagebox.showerror("Error", "Autor no encontrado")

    def actualizar_autor(self):
        try:
            self.comunicacion.actualizar_autor(
                self.autor.id.get(), self.autor.nombre.get(),
                self.autor.nacionalidad.get(), int(self.autor.edad.get())
            )
            messagebox.showinfo("Éxito", "Autor actualizado correctamente")
            self.consultar_todos_autores()
        except Exception as e:
            messagebox.showerror("Error", f"Datos inválidos: {e}")

    def eliminar_autor(self):
        id_ = self.autor.id.get()
        if not id_:
            return messagebox.showwarning("Aviso", "Ingrese un ID")
        self.comunicacion.eliminar_autor(id_)
        messagebox.showinfo("Éxito", "Autor eliminado correctamente")
        self.consultar_todos_autores()
        self.limpiar_autor()

    def limpiar_autor(self):
        for var in [self.autor.id, self.autor.nombre, self.autor.nacionalidad, self.autor.edad]:
            var.set("")

    def consultar_todos_autores(self):
        autores = self.comunicacion.obtener_autores()
        data = [(a['id'], a['nombre'], a['nacionalidad'], a['edad']) for a in autores]
        self.tabla_autores.refrescar(data)

    # LIBROS
    def crear_ventana_libro(self):
        tk.Label(self.libro_tab, text="LIBRO", font=("Arial", 22), bg="#D6EAF8").pack(pady=10)
        frame = tk.LabelFrame(self.libro_tab, text="Datos del libro", padx=10, pady=10, bg="#D6EAF8")
        frame.place(x=20, y=60, width=300, height=250)

        campos = [("ID", self.libro.id), ("Título", self.libro.titulo),
                  ("Género", self.libro.genero), ("Páginas", self.libro.paginas),
                  ("Año de publicación", self.libro.año_publicacion)]

        for i, (label, var) in enumerate(campos):
            tk.Label(frame, text=f"{label}:", anchor="w", bg="#D6EAF8").grid(row=i, column=0, sticky="w", pady=2)
            tk.Entry(frame, width=25, textvariable=var).grid(row=i, column=1, pady=2)

        btn_frame = tk.Frame(self.libro_tab, bg="#D6EAF8")
        btn_frame.place(x=20, y=320)
        botones = ["Enviar", "Consultar", "Actualizar", "Eliminar", "Limpiar", "Consultar Todos"]
        funciones = [self.guardar_libro, self.consultar_libro, self.actualizar_libro,
                     self.eliminar_libro, self.limpiar_libro, self.consultar_todos_libros]
        for i, (texto, funcion) in enumerate(zip(botones, funciones)):
            tk.Button(btn_frame, text=texto, width=15, command=funcion).grid(row=i // 2, column=i % 2, padx=5, pady=3)
        columnas = ["ID", "TÍTULO", "GÉNERO", "PÁGINAS", "AÑO DE PUBLICACIÓN"]
        self.tabla_libros = Tabla(self.libro_tab, columnas, columnas, [])
        self.tabla_libros.tabla.place(x=350, y=60, width=800, height=550)


        for col, ancho in zip(columnas, [50, 250, 150, 100, 150]):
         self.tabla_libros.tabla.column(col, width=ancho)



    def guardar_libro(self):
        try:
            self.comunicacion.guardar_libro(
                self.libro.titulo.get(), self.libro.genero.get(),
                int(self.libro.paginas.get()), int(self.libro.año_publicacion.get())
            )
            messagebox.showinfo("Éxito", "Libro guardado correctamente")
            self.consultar_todos_libros()
        except Exception as e:
            messagebox.showerror("Error", f"Datos inválidos: {e}")

    def consultar_libro(self):
        id_ = self.libro.id.get()
        if not id_:
            return messagebox.showwarning("Aviso", "Ingrese un ID")
        libro = self.comunicacion.consultar_libro(id_)
        if libro:
            self.libro.id.set(libro['id'])
            self.libro.titulo.set(libro['titulo'])
            self.libro.genero.set(libro['genero'])
            self.libro.paginas.set(libro['paginas'])
            self.libro.año_publicacion.set(libro['año_publicacion'])
        else:
            messagebox.showerror("Error", "Libro no encontrado")

    def actualizar_libro(self):
        try:
            self.comunicacion.actualizar_libro(
                self.libro.id.get(), self.libro.titulo.get(), self.libro.genero.get(),
                int(self.libro.paginas.get()), int(self.libro.año_publicacion.get())
            )
            messagebox.showinfo("Éxito", "Libro actualizado correctamente")
            self.consultar_todos_libros()
        except Exception as e:
            messagebox.showerror("Error", f"Datos inválidos: {e}")

    def eliminar_libro(self):
        id_ = self.libro.id.get()
        if not id_:
            return messagebox.showwarning("Aviso", "Ingrese un ID")
        self.comunicacion.eliminar_libro(id_)
        messagebox.showinfo("Éxito", "Libro eliminado correctamente")
        self.consultar_todos_libros()
        self.limpiar_libro()

    def limpiar_libro(self):
        for var in [self.libro.id, self.libro.titulo, self.libro.genero, self.libro.paginas, self.libro.año_publicacion]:
            var.set("")

    def consultar_todos_libros(self):
        libros = self.comunicacion.obtener_libros()
        data = [(l['id'], l['titulo'], l['genero'], l['paginas'], l['año_publicacion']) for l in libros]
        self.tabla_libros.refrescar(data)
