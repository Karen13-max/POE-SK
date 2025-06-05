import tkinter as tk

class Libro():
    def __init__(self, ventanaPrincipal):
        self.ventanaPrincipal = ventanaPrincipal
        self.id = tk.StringVar(ventanaPrincipal)
        self.titulo = tk.StringVar(ventanaPrincipal)
        self.genero = tk.StringVar(ventanaPrincipal)
        self.paginas = tk.StringVar(ventanaPrincipal)
        self.año_publicacion = tk.StringVar(ventanaPrincipal)