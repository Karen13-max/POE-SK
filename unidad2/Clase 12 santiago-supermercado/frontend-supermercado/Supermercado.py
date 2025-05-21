import tkinter as tk
from tkinter import messagebox

import requests

# Funciones de ejemplo para cada botón
    
# SE DEFINE LA FUNCION PARA GUARDAR LOS DATOS EN LA API
def guardar(nombre, precio, cantidad, id_cliente):

    datos = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad,
        "id_cliente": id_cliente,
    }
    
    respuesta = requests.post("http://127.0.0.1:8000/api/productos/", json=datos)
    if respuesta.status_code == 201:
        print("Datos guardados correctamente.")
    else:
        print("Error al guardar los datos.")
    messagebox.showinfo("Guardar", f"Guardando:\nProducto: {entrada_producto.get()}\nValor: {entrada_valor.get()}\nCantidad: {entrada_cantidad.get()}\nID Cliente: {entrada_id_cliente.get()}")


# Definimos la función para consultar los datos de la API
def consultar():
    request = requests.get("http://127.0.0.1:8000/api/productos/")
    
    if request.status_code == 200:
        datos = request.json()
        id_buscar = entrada_documento.get()

        for producto in datos:
            # Convertimos ambos a string para evitar errores de comparación
            if str(producto.get("id")) == str(id_buscar):
                entrada_producto.delete(0, tk.END)
                entrada_valor.delete(0, tk.END)
                entrada_cantidad.delete(0, tk.END)
                entrada_id_cliente.delete(0, tk.END)

                entrada_producto.insert(0, producto.get("nombre", ""))
                entrada_valor.insert(0, producto.get("precio", ""))
                entrada_cantidad.insert(0, producto.get("cantidad", ""))
                entrada_id_cliente.insert(0, producto.get("id_cliente", ""))

                messagebox.showinfo("Consultar", f"Producto: {producto['nombre']}\nValor: {producto['precio']}\nCantidad: {producto['cantidad']}\nID Cliente: {producto['id_cliente']}")
                return

        messagebox.showinfo("Consultar", "No se encontró el producto.")
    else:
        messagebox.showerror("Error", f"No se pudo conectar con la API. Código: {request.status_code}")


# Se define la función para actualizar los datos en la API
def actualizar():
    id_producto = entrada_documento.get().strip()
    datos_actualizados = {
        "nombre": entrada_producto.get(),
        "precio": entrada_valor.get(),
        "cantidad": entrada_cantidad.get(),
        "id_cliente": entrada_id_cliente.get(),
    }
    response = requests.put(f"http://127.0.0.1:8000/api/productos/{id_producto}/", json=datos_actualizados)
    if response.status_code == 200:
        messagebox.showinfo("Actualizar", "Producto actualizado correctamente.")
    else:
        messagebox.showerror("Actualizar", f"No se pudo actualizar el producto. Código: {response.status_code}")


#se define la función para eliminar los datos en la API
def eliminar():
    id_producto = entrada_documento.get().strip()

    if not id_producto:
        messagebox.showwarning("Eliminar", "Por favor ingresa un ID válido.")
        return

    confirmar = messagebox.askyesno("Confirmar eliminación", f"¿Estás seguro de eliminar el producto con ID {id_producto}?")

    if confirmar:
        response = requests.delete(f"http://127.0.0.1:8000/api/productos/{id_producto}/")

        if response.status_code == 204:
            messagebox.showinfo("Eliminar", "Producto eliminado correctamente.")
            # Limpiar campos después de eliminar
            entrada_producto.delete(0, tk.END)
            entrada_valor.delete(0, tk.END)
            entrada_cantidad.delete(0, tk.END)
            entrada_id_cliente.delete(0, tk.END)
            entrada_documento.delete(0, tk.END)
        else:
            messagebox.showerror("Eliminar", f"No se pudo eliminar el producto. Código: {response.status_code}")




# Crear ventana principal
ventana = tk.Tk()
ventana.title("Gestión de Productos")
ventana.geometry("400x300")

# Documento
tk.Label(ventana, text="id:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entrada_documento = tk.Entry(ventana, width=30)
entrada_documento.grid(row=0, column=1, padx=10, pady=5)
tk.Button(ventana, text="Consultar", command=consultar).grid(row=0, column=2, padx=10)

# Producto
tk.Label(ventana, text="Producto:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
entrada_producto = tk.Entry(ventana, width=30)
entrada_producto.grid(row=1, column=1, columnspan=2, padx=10, pady=5)

# Valor del producto
tk.Label(ventana, text="Valor del producto:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
entrada_valor = tk.Entry(ventana, width=30)
entrada_valor.grid(row=2, column=1, columnspan=2, padx=10, pady=5)

# Cantidad
tk.Label(ventana, text="Cantidad:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
entrada_cantidad = tk.Entry(ventana, width=30)
entrada_cantidad.grid(row=3, column=1, columnspan=2, padx=10, pady=5)

# id_cliente
tk.Label(ventana, text="id cliente:").grid(row=4, column=0, padx=10, pady=5, sticky="e")
entrada_id_cliente = tk.Entry(ventana, width=30)
entrada_id_cliente.grid(row=4, column=1, columnspan=2, padx=10, pady=5)

# Botones Guardar, Actualizar, Eliminar
tk.Button(ventana, text="Guardar", command=lambda: guardar(
    entrada_producto.get(),
    entrada_valor.get(),
    entrada_cantidad.get(),
    entrada_id_cliente.get()
), width=10).grid(row=5, column=1, pady=10, sticky="w")

tk.Button(ventana, text="Actualizar", command=actualizar, width=10).grid(row=5, column=1, pady=10)
tk.Button(ventana, text="Eliminar", command=eliminar, width=10).grid(row=5, column=1, pady=10, sticky="e")

# Ejecutar el bucle principal
ventana.mainloop()