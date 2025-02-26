from tkinter import Frame, Tk 
from tkinter.messagebox import askyesno

ventanaPrincipal = Tk()
ventanaPrincipal.title("Prueba de eventos")

def accion_Click(event):
    frame.focus_set()
    print("clicked at", event.x, event.y)

def precionar_tecla(event):
    print("pressed", repr(event.char))

def el_usuario_quiere_salir():
    if askyesno("Salir", "¿Estás seguro de que deseas salir?"):
        ventanaPrincipal.destroy()

frame = Frame(ventanaPrincipal, width=500, height=500)
frame.bind("<Key>", precionar_tecla)
frame.bind("<Button-1>", accion_Click)
frame.pack()

ventanaPrincipal.protocol("WM_DELETE_WINDOW", el_usuario_quiere_salir)
ventanaPrincipal.mainloop()

