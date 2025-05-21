import tkinter as tk
from controladores.comunicacion import Comunicacion
from modelos.producto import Producto
from .tabla import Tabla

class Interfaz():

    def __init__(self):
        titulos = ['Id', 'Nombre', 'Precio', 'Cantidad', 'id_cliente']
        columnas = ['Id', 'Nombre', 'Precio', 'Cantidad', 'id_cliente']
        data = []
        self.ventanaPrincipal = tk.Tk()
        self.comunicacion = Comunicacion(self.ventanaPrincipal)
        self.tabla = Tabla(self.ventanaPrincipal, titulos, columnas, data)
        pass

    def accion_guardar_boton(self, id, nombre, precio, cantidad, id_cliente):
        if id == '':
            self.comunicacion.guardar(nombre, precio, cantidad, id_cliente)
        else:
            self.comunicacion.actualizar(id, nombre, precio, cantidad, id_cliente)

    def accion_consultar_boton(self, labelConsulta, id):
        resultado = self.comunicacion.consultar(id)
        labelConsulta.config(text = "Nombre: " + str(resultado.get('nombre')) + " " + "Precio: " + str(resultado.get('precio')) + " " + "Cantidad: " + str(resultado.get('cantidad')) + " " + "ID Cliente: " + str(resultado.get('id_cliente')))

    def accion_consultar_todo(self, nombre, precio, cantidad, id_cliente):
        resultado = self.comunicacion.consultar_todo(nombre, precio, cantidad, id_cliente)
        data = []
        for elemento in resultado:
            data.append((elemento.get('id'), elemento.get('nombre'), elemento.get('precio'), elemento.get('cantidad'), elemento.get('id_cliente')))
        self.tabla.refrescar(data)
        print(data)

    def mostrar_interfaz(self):
        producto = Producto(self.ventanaPrincipal)

        labelId = tk.Label(self.ventanaPrincipal, text="Id")
        entryId = tk.Entry(self.ventanaPrincipal, textvariable=producto.id)
        labelNombre = tk.Label(self.ventanaPrincipal, text="Nombre")
        entryNombre = tk.Entry(self.ventanaPrincipal, textvariable=producto.nombre)
        labelPrecio = tk.Label(self.ventanaPrincipal, text="Precio")
        entryPrecio = tk.Entry(self.ventanaPrincipal, textvariable=producto.precio)
        labelCantidad = tk.Label(self.ventanaPrincipal, text="Cantidad")
        entryCantidad = tk.Entry(self.ventanaPrincipal, textvariable=producto.cantidad)
        labelIdCliente = tk.Label(self.ventanaPrincipal, text="Id Cliente")
        entryIdCliente = tk.Entry(self.ventanaPrincipal, textvariable=producto.id_cliente)
        labelConsulta = tk.Label(self.ventanaPrincipal, text='')
        
        boton_guardar = tk.Button(self.ventanaPrincipal, 
                   text="Guardar", 
                   command=lambda: self.accion_guardar_boton(entryId.get(), entryNombre.get(), entryPrecio.get(), entryCantidad.get(), entryIdCliente.get()))
        
        boton_consultar_1 = tk.Button(self.ventanaPrincipal, 
                   text="Consultar 1", 
                   command=lambda: self.accion_consultar_boton(labelConsulta, entryId.get()))
        
        boton_consultar_todos = tk.Button(self.ventanaPrincipal, 
                   text="Consultar todos", 
                   command=lambda: self.accion_consultar_todo(entryNombre.get(), entryPrecio.get(), entryCantidad.get(), entryIdCliente.get()))

        #creando la ventana
        self.ventanaPrincipal.title("Ventana Principal")
        self.ventanaPrincipal.geometry("1000x600")
        labelId.pack()
        entryId.pack()
        labelNombre.pack()
        entryNombre.pack()
        labelPrecio.pack()
        entryPrecio.pack()
        labelCantidad.pack()
        entryCantidad.pack()
        labelIdCliente.pack()
        entryIdCliente.pack()
        boton_guardar.pack()
        boton_consultar_1.pack()
        boton_consultar_todos.pack()
        labelConsulta.pack()
        self.tabla.tabla.pack()

        def seleccionar_elemento(_):
            for i in self.tabla.tabla.selection():
                valores = self.tabla.tabla.item(i)['values']
                entryId.delete(0, tk.END)
                entryId.insert(0, str(valores[0]))
                entryNombre.delete(0, tk.END)
                entryNombre.insert(0, str(valores[1]))
                entryPrecio.delete(0, tk.END)
                entryPrecio.insert(0, str(valores[2]))
                entryCantidad.delete(0, tk.END)
                entryCantidad.insert(0, str(valores[3]))
                entryIdCliente.delete(0, tk.END)
                entryIdCliente.insert(0, str(valores[4]))

        def borrar_elemento(_):
            for i in self.tabla.tabla.selection():
                self.comunicacion.eliminar(self.tabla.tabla.item(i)['values'][0])
                self.tabla.tabla.delete(i)

        self.tabla.tabla.bind('<<TreeviewSelect>>', seleccionar_elemento)
        self.tabla.tabla.bind('<Delete>', borrar_elemento)

        self.ventanaPrincipal.mainloop()