
import tkinter as tk
from tkinter import messagebox
import requests

# URL del backend Django
API_URL = "http://127.0.0.1:8000/api/productos/"

# Funciones
def consultar():
    id_ = id_entry.get()
    if not id_:
        messagebox.showwarning("Error", "Por favor ingresa un ID para consultar.")
        return
    response = requests.get(API_URL + id_)
    if response.status_code == 200:
        data = response.json()
        nombre_entry.delete(0, tk.END)
        valor_entry.delete(0, tk.END)
        edad_entry.delete(0, tk.END)
        id_cliente_entry.delete(0, tk.END)

        nombre_entry.insert(0, data.get("nombre", ""))
        valor_entry.insert(0, data.get("valor_entrada", ""))
        edad_entry.insert(0, data.get("edad", ""))
        id_cliente_entry.insert(0, data.get("id_cliente", ""))
    else:
        messagebox.showerror("Error", f"No se encontró el producto con ID {id_}.")

def guardar():
    data = {
        "nombre": nombre_entry.get(),
        "valor_entrada": valor_entry.get(),
        "edad": edad_entry.get(),
        "id_cliente": id_cliente_entry.get()
    }
    response = requests.post(API_URL, json=data)
    if response.status_code == 201:
        messagebox.showinfo("Éxito", "Producto guardado correctamente.")
    else:
        messagebox.showerror("Error", "No se pudo guardar el producto.")

def actualizar():
    id_ = id_entry.get()
    if not id_:
        messagebox.showwarning("Error", "Debes ingresar el ID para actualizar.")
        return
    data = {
        "nombre": nombre_entry.get(),
        "valor_entrada": valor_entry.get(),
        "edad": edad_entry.get(),
        "id_cliente": id_cliente_entry.get()
    }
    response = requests.put(API_URL + id_ + "/", json=data)
    if response.status_code == 200:
        messagebox.showinfo("Éxito", "Producto actualizado correctamente.")
    else:
        messagebox.showerror("Error", "No se pudo actualizar el producto.")

def eliminar():
    id_ = id_entry.get()
    if not id_:
        messagebox.showwarning("Error", "Debes ingresar el ID para eliminar.")
        return
    response = requests.delete(API_URL + id_ + "/")
    if response.status_code == 204:
        messagebox.showinfo("Éxito", "Producto eliminado correctamente.")
        nombre_entry.delete(0, tk.END)
        valor_entry.delete(0, tk.END)
        edad_entry.delete(0, tk.END)
        id_cliente_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "No se pudo eliminar el producto.")

# Crear ventana
ventana = tk.Tk()
ventana.title("Gestión de Productos")
ventana.geometry("450x350")

# Campos
tk.Label(ventana, text="ID").grid(row=0, column=0, padx=10, pady=5, sticky="w")
id_entry = tk.Entry(ventana)
id_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Button(ventana, text="Consultar", command=consultar).grid(row=0, column=2, padx=10)

tk.Label(ventana, text="Nombre").grid(row=1, column=0, padx=10, pady=5, sticky="w")
nombre_entry = tk.Entry(ventana)
nombre_entry.grid(row=1, column=1, columnspan=2, padx=10, pady=5)

tk.Label(ventana, text="Valor entrada").grid(row=2, column=0, padx=10, pady=5, sticky="w")
valor_entry = tk.Entry(ventana)
valor_entry.grid(row=2, column=1, columnspan=2, padx=10, pady=5)

tk.Label(ventana, text="Edad").grid(row=3, column=0, padx=10, pady=5, sticky="w")
edad_entry = tk.Entry(ventana)
edad_entry.grid(row=3, column=1, columnspan=2, padx=10, pady=5)

tk.Label(ventana, text="ID Cliente").grid(row=4, column=0, padx=10, pady=5, sticky="w")
id_cliente_entry = tk.Entry(ventana)
id_cliente_entry.grid(row=4, column=1, columnspan=2, padx=10, pady=5)

# Botones
tk.Button(ventana, text="Guardar", command=guardar).grid(row=5, column=0, pady=20)
tk.Button(ventana, text="Actualizar", command=actualizar).grid(row=5, column=1)
tk.Button(ventana, text="Eliminar", command=eliminar).grid(row=5, column=2)

ventana.mainloop()
