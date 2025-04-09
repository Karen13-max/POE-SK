
root = tk.Tk()
root.title("Zoológico")
root.geometry("400x500")

def validar_numeros(event, entrada, etiqueta_error, mensaje):
    if entrada.get().isdigit() or entrada.get() == "":
        etiqueta_error.config(text="", fg="black")
    else:
        etiqueta_error.config(text=mensaje)


def validar_letras(event, entrada, etiqueta_error):
    if entrada.get().replace(" ", "").isalpha() or entrada.get() == "":
        etiqueta_error.config(text="", fg="black")
    else:
        etiqueta_error.config(text="Solo se permiten letras y espacios")

def verificar_valor(event):
    validar_numeros(event, entrada_valor, error_valor, "Solo números")

def verificar_nombre(event):
    validar_letras(event, entrada_nombre, error_nombre)

def verificar_documento(event):
    validar_numeros(event, entrada_documento, error_documento, "Solo números")

def verificar_edad(event):
    validar_numeros(event, entrada_edad, error_edad, "Solo números")

# --- Valor de entrada ---
tk.Label(root, text="Valor de entrada", font=("Arial", 14)).pack(pady=5)
entrada_valor = tk.Entry(root, font=("Arial", 12))
entrada_valor.pack(pady=5)
error_valor = tk.Label(root, text="", font=("Arial", 10), fg="black")
error_valor.pack()
entrada_valor.bind("<KeyRelease>", verificar_valor)

# --- Nombre del visitante ---
tk.Label(root, text="Nombre del Visitante", font=("Arial", 14)).pack(pady=5)
entrada_nombre = tk.Entry(root, font=("Arial", 12))
entrada_nombre.pack(pady=5)
error_nombre = tk.Label(root, text="", font=("Arial", 10), fg="black")
error_nombre.pack()
entrada_nombre.bind("<KeyRelease>", verificar_nombre)

# --- Documento ---
tk.Label(root, text="Documento", font=("Arial", 14)).pack(pady=5)
entrada_documento = tk.Entry(root, font=("Arial", 12))
entrada_documento.pack(pady=5)
error_documento = tk.Label(root, text="", font=("Arial", 10), fg="black")
error_documento.pack()
entrada_documento.bind("<KeyRelease>", verificar_documento)

# --- Edad ---
tk.Label(root, text="Edad", font=("Arial", 14)).pack(pady=5)
entrada_edad = tk.Entry(root, font=("Arial", 12))
entrada_edad.pack(pady=5)
error_edad = tk.Label(root, text="", font=("Arial", 10), fg="black")
error_edad.pack()
entrada_edad.bind("<KeyRelease>", verificar_edad)


boton_salir = tk.Button(root, text="Salir", font=("Arial", 14), command=root.destroy)
boton_salir.pack(pady=10)


root.mainloop()
