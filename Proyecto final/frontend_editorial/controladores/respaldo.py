import threading
import time # tiempo para el respaldo automático
import requests
import os
from datetime import datetime

API_URL = "http://127.0.0.1:8000/api" 
BACKUP_INTERVAL = 10# segundos
stop_event = threading.Event()

def respaldos_automaticos():
   # Crear la carpeta de respaldos si no existe
    ruta_respaldos = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'respaldos')
    os.makedirs(ruta_respaldos, exist_ok=True)


    # Ruta del archivo de resumen general
    archivo_resumen = os.path.join(ruta_respaldos, "resumen_respaldo.txt")

    while not stop_event.is_set():
        try:
            time.sleep(BACKUP_INTERVAL)
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # Formato de fecha y hora
            nombre_timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")# Formato de fecha y hora para el nombre del archivo, (para que no se creen archivos con el mismo nombre)

            archivo_autores = os.path.join(ruta_respaldos, f"autores_{nombre_timestamp}.txt")
            archivo_libros = os.path.join(ruta_respaldos, f"libros_{nombre_timestamp}.txt")

            with open(archivo_resumen, "a", encoding="utf-8") as resumen:
                resumen.write(f"\n🔁 Iniciando respaldo automático ({timestamp})\n")
                print(f"\n🔁 Iniciando respaldo automático ({timestamp})")

                # Respaldar autores
                r_autores = requests.get(f"{API_URL}/autores/")
                if r_autores.status_code == 200:
                    with open(archivo_autores, "w", encoding="utf-8") as f:
                        for a in r_autores.json():
                            texto = (
                                f"ID: {a['id']}\n"
                                f"Nombre: {a['nombre']}\n"
                                f"Nacionalidad: {a['nacionalidad'].capitalize()}\n"
                                f"Edad: {a['edad']}\n\n"
                            )
                            f.write(texto)
                            resumen.write(f"[Autor respaldado]\n{texto}")
                            print(f"[Autor respaldado]\n{texto.strip()}")

                # Respaldar libros
                r_libros = requests.get(f"{API_URL}/libros/")
                if r_libros.status_code == 200:
                    with open(archivo_libros, "w", encoding="utf-8") as f:
                        for l in r_libros.json():
                            texto = (
                                f"ID: {l['id']}\n"
                                f"Título: {l['titulo']}\n"
                                f"Género: {l['genero']}\n"
                                f"Páginas: {l['paginas']}\n"
                                f"Año_publicacion: {l['año_publicacion']}\n\n"
                            )
                            f.write(texto)
                            resumen.write(f"[Libro respaldado]\n{texto}")
                            print(f"[Libro respaldado]\n{texto.strip()}")

                resumen.write(f"Respaldo completado correctamente ({timestamp})\n")
                print(f" Respaldo completado correctamente ({timestamp})")

        except Exception as e:
            mensaje_error = f"Error durante el respaldo: {e}"
            print(mensaje_error)
            with open(archivo_resumen, "a", encoding="utf-8") as resumen:
                resumen.write(mensaje_error + "\n")
            time.sleep(5)

# Función para iniciar el hilo de respaldo automático
def iniciar_hilo_respaldo():
    hilo = threading.Thread(target=respaldos_automaticos, daemon=True)
    hilo.start()

