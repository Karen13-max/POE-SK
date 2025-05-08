import tkinter as tk
import requests
from tkinter import messagebox

# --- Funciones ---
def guardar():
    datos = {
        "documento": entrada_documento.get(),
        "producto": entrada_nombre.get(),
        "valor_del_producto": entrada_valor.get(),
        "cantidad": entrada_edad.get(),
    }
    respuesta = requests.post("http://127.0.0.1:8000/api/productos/", json=datos)
    if respuesta.status_code == 201:
        messagebox.showinfo("Éxito", "Datos guardados correctamente.")
    else:
        messagebox.showerror("Error", "No se pudieron guardar los datos.")

def consultar():
    respuesta = requests.get("http://127.0.0.1:8000/api/productos/")
    if respuesta.status_code == 200:
        productos = respuesta.json()
        resultado = ""
        for p in productos:
            resultado += f"Doc: {p['documento']} - Producto: {p['producto']} - Valor: {p['valor_del_producto']} - Cantidad: {p['cantidad']}\n"
        messagebox.showinfo("Productos", resultado)
    else:
        messagebox.showerror("Error", "No se pudieron consultar los datos.")

def limpiar():
    entrada_documento.delete(0, tk.END)
    entrada_nombre.delete(0, tk.END)
    entrada_valor.delete(0, tk.END)
    entrada_edad.delete(0, tk.END)

def validar_numeros(event, entrada, etiqueta_error, mensaje):
    if entrada.get().isdigit() or entrada.get() == "":
        etiqueta_error.config(text="", fg="black")
    else:
        etiqueta_error.config(text=mensaje)

def validar_letras(event, entrada, etiqueta_error):
    if entrada.get().replace(" ", "").isalpha() or entrada.get() == "":
        etiqueta_error.config(text="", fg="black")
    else:
        etiqueta_error.config(text="Solo letras y espacios")

def verificar_valor(event):
    validar_numeros(event, entrada_valor, error_valor, "Solo números")

def verificar_nombre(event):
    validar_letras(event, entrada_nombre, error_nombre)

def verificar_documento(event):
    validar_numeros(event, entrada_documento, error_documento, "Solo números")

def verificar_edad(event):
    validar_numeros(event, entrada_edad, error_edad, "Solo números")

# --- Ventana principal ---
root = tk.Tk()
root.title("Supermercado")
root.geometry("400x550")

# --- Campos de entrada ---
tk.Label(root, text="Documento", font=("Arial", 14)).pack(pady=5)
entrada_documento = tk.Entry(root, font=("Arial", 12))
entrada_documento.pack(pady=5)
error_documento = tk.Label(root, text="", font=("Arial", 10))
error_documento.pack()
entrada_documento.bind("<KeyRelease>", verificar_documento)

tk.Label(root, text="Producto", font=("Arial", 14)).pack(pady=5)
entrada_nombre = tk.Entry(root, font=("Arial", 12))
entrada_nombre.pack(pady=5)
error_nombre = tk.Label(root, text="", font=("Arial", 10))
error_nombre.pack()
entrada_nombre.bind("<KeyRelease>", verificar_nombre)

tk.Label(root, text="Valor del producto", font=("Arial", 14)).pack(pady=5)
entrada_valor = tk.Entry(root, font=("Arial", 12))
entrada_valor.pack(pady=5)
error_valor = tk.Label(root, text="", font=("Arial", 10))
error_valor.pack()
entrada_valor.bind("<KeyRelease>", verificar_valor)

tk.Label(root, text="Cantidad", font=("Arial", 14)).pack(pady=5)
entrada_edad = tk.Entry(root, font=("Arial", 12))
entrada_edad.pack(pady=5)
error_edad = tk.Label(root, text="", font=("Arial", 10))
error_edad.pack()
entrada_edad.bind("<KeyRelease>", verificar_edad)

# --- Botones ---
tk.Button(root, text="Guardar", font=("Arial", 14), command=guardar).pack(pady=10)
tk.Button(root, text="Consultar", font=("Arial", 14), command=consultar).pack(pady=10)
tk.Button(root, text="Limpiar", font=("Arial", 14), command=limpiar).pack(pady=10)
tk.Button(root, text="Salir", font=("Arial", 14), command=root.destroy).pack(pady=10)

root.mainloop()