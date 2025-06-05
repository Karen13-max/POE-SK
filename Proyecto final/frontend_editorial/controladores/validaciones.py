import re

class Validaciones:

    def validar_letras(valor):
        patron = re.compile("^[A-Za-zñÑáéíóúÁÉÍÓÚ ]*$")
        resultado = patron.match(valor.strip()) is not None
        return resultado

   
    def validar_numeros(valor):
        patron = re.compile("^\d+$")
        resultado = patron.match(valor.strip()) is not None
        return resultado

    def validar_no_vacio(valor):
        return bool(valor.strip())
