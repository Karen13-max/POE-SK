import tkinter as tk

class Producto():
        
    def __init__(self, ventanaPrincipal):
        self.ventanaPrincipal = ventanaPrincipal
        self.id = tk.StringVar(ventanaPrincipal)
        self.nombre = tk.StringVar(ventanaPrincipal)
        self.precio = tk.StringVar(ventanaPrincipal)
        self.cantidad = tk.StringVar(ventanaPrincipal)
        self.id_cliente = tk.StringVar(ventanaPrincipal)