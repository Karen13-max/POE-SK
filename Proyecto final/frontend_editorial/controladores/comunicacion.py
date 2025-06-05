import requests

class Comunicacion:
    def __init__(self, ventanaPrincipal=None):
        self.base_url = 'http://127.0.0.1:8000/api/'
        
     
        
        self.ventanaPrincipal = ventanaPrincipal

    # Métodos para AUTOR

    
    def obtener_autores(self):
        try:
            response = requests.get(self.base_url + "autores/")
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Error al obtener autores. Código: {response.status_code}")
                print(f"Respuesta del servidor: {response.text}")
                return []
        except Exception as e:
            print(f"Error en obtener_autores: {e}")
            return []
    
    def guardar_autor(self, nombre, nacionalidad, edad):
        try:
            data = {
                'nombre': nombre,
                'nacionalidad': nacionalidad,
                'edad': int(edad)
            }
            resultado = requests.post(self.base_url + 'autores/', json=data)
            print(resultado.json())
            return resultado
        except Exception as e:
            print(f"Error: {e}")

    def actualizar_autor(self, id, nombre, nacionalidad, edad):
        try:
            data = {
                'nombre': nombre,
                'nacionalidad': nacionalidad,
                'edad': int(edad)
            }
            resultado = requests.put(self.base_url + f'autores/{id}/', json=data)
            print(resultado.json())
            return resultado
        except Exception as e:
            print(f"Error: {e}")

    def consultar_autor(self, id):
        try:
            resultado = requests.get(self.base_url + f'autores/{id}/')
            return resultado.json()
        except Exception as e:
            print(f"Error: {e}")

    def consultar_todos_autores(self):
        try:
            resultado = requests.get(self.base_url + 'autores/')
            return resultado.json()
        except Exception as e:
            print(f"Error: {e}")

    def eliminar_autor(self, id):
        try:
            resultado = requests.delete(self.base_url + f'autores/{id}/')
            return resultado.status_code
        except Exception as e:
            print(f"Error: {e}")

    # Métodos para LIBRO
    
    def obtener_libros(self):
        try:
            response = requests.get(self.base_url + "libros/")
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Error al obtener libros. Código: {response.status_code}")
                print(f"Respuesta del servidor: {response.text}")
                return []
        except Exception as e:
            print(f"Error en obtener_libros: {e}")
            return []

    def guardar_libro(self, titulo, genero, paginas, año_publicacion):
        try:
            data = {
                'titulo': titulo,
                'genero': genero,
                'paginas': int(paginas),
                'año_publicacion': int(año_publicacion)
            }
            resultado = requests.post(self.base_url + 'libros/', json=data)
            print(resultado.json())
            return resultado
        except Exception as e:
            print(f"Error: {e}")

    def actualizar_libro(self, id, titulo, genero, paginas, año_publicacion):
        try:
            data = {
                'titulo': titulo,
                'genero': genero,
                'paginas': int(paginas),
                'año_publicacion': int(año_publicacion)
            }
            resultado = requests.put(self.base_url + f'libros/{id}/', json=data)
            print(resultado.json())
            return resultado
        except Exception as e:
            print(f"Error: {e}")

    def consultar_libro(self, id):
        try:
            resultado = requests.get(self.base_url + f'libros/{id}/')
            return resultado.json()
        except Exception as e:
            print(f"Error: {e}")

    def consultar_todos_libros(self):
        try:
            resultado = requests.get(self.base_url + 'libros/')
            return resultado.json()
        except Exception as e:
            print(f"Error: {e}")

    def eliminar_libro(self, id):
        try:
            resultado = requests.delete(self.base_url + f'libros/{id}/')
            return resultado.status_code
        except Exception as e:
            print(f"Error: {e}")
