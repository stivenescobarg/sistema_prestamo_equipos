# ============================================================
# Ejemplo 28: Base y Derivada - Métodos privados en herencia
# Descripción: Comportamiento de métodos privados con herencia.
# ============================================================

class Base:
    def __init__(self):
        self.publico = "Accesible para todos"

    def metodo_publico(self):
        print("Método público llamando a método privado:")
        self.__metodo_privado()

    def __metodo_privado(self):
        print("Este es un método privado de Base")

class Derivada(Base):
    def nuevo_metodo(self):
        print("Intentando llamar al método privado del padre:")
        try:
            self.__metodo_privado()  # Esto fallará
        except AttributeError as e:
            print(f"Error: {e}")

    def __metodo_privado(self):
        print("Este es un método privado de Derivada")


base = Base()
base.metodo_publico()  # Funciona correctamente

derivada = Derivada()
derivada.metodo_publico()  # Funciona, llama al __metodo_privado de Base
derivada.nuevo_metodo()  # Falla al intentar llamar a __metodo_privado de Base