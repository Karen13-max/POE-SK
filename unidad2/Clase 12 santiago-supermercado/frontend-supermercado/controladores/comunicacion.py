import requests

class Comunicacion():

    def __init__(self, ventanaPrincipal):
        self.url = 'http://localhost:8000/api/productos/'
        self.ventanaPrincipal = ventanaPrincipal
        pass

    def guardar(self, nombre, precio, cantidad, id_cliente):
        try:
            print(nombre, precio, cantidad, id_cliente)
            data = {
                'nombre': nombre,
                'precio': precio,
                'cantidad': cantidad,
                'id_cliente': id_cliente
            }
            resultado = requests.post(self.url, json=data)
            print(resultado.json())
            return resultado
        except:
            pass

    def actualizar(self, id, nombre, precio, cantidad, id_cliente):
        try:
            print(nombre, precio, cantidad, id_cliente)
            data = {
                'nombre': nombre,
                'precio': precio,
                'cantidad': cantidad,
                'id_cliente': id_cliente
            }
            resultado = requests.put(self.url + str(id)+ '/', json=data)
            print(resultado.json)
            return resultado
        except:
            pass
    
    def consultar(self, id):
        resultado = requests.get(self.url + str(id))
        return resultado.json()
    
    def consultar_todo(self, nombre, precio, cantidad, id_cliente):
        url = self.url+ "?"

        if nombre != '':
            url = url + "nombre=" + str(nombre) + "&"
        if precio != '':
            url = url + 'precio=' + str(precio) + "&"
        if cantidad != '':
            url = url + 'cantidad=' + str(cantidad) + "&"
        if id_cliente != '':
            url = url + 'id_cliente=' + str(id_cliente) + "&"

        print(url)
        resultado = requests.get(url)
        return resultado.json()
    
    def eliminar(self, id):
        resultado = requests.delete(self.url + str(id))
        return resultado.status_code