
import tkinter as tk
from vistas.Interfaz import BibliotecaApp
from controladores.respaldo import iniciar_hilo_respaldo, stop_event

# Iniciar hilo de respaldo
iniciar_hilo_respaldo()

# Configuración de la ventana principal
def main():
    root = tk.Tk()
    root.title("Mi Biblioteca")
    root.geometry("400x300")

     


   

    # Evento para detener el hilo de respaldo al cerrar la ventana
    stop_event.set()
    
    # Función para manejar el cierre de la ventana
    def al_cerrar():
        stop_event.set()
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", al_cerrar) 
      
# --------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = BibliotecaApp(root)
    root.mainloop()