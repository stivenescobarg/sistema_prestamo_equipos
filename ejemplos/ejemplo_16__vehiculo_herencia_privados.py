# ============================================================
# Ejemplo 16: Vehiculo - Atributos privados vs protegidos en herencia
# Descripción: Diferencia entre _ (protegido) y __ (privado).
# ============================================================

class Vehiculo:
    def __init__(self, marca, modelo):
        self._marca = marca      # Protegido (convención)
        self.__modelo = modelo   # Privado (name mangling)

class Coche(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self._puertas = puertas

    def info(self):
        # Podemos acceder a _marca (protegido)
        print(f"Marca: {self._marca}")

        # Esto generará un AttributeError
        try:
            print(f"Modelo: {self.__modelo}")
        except AttributeError:
            print("No se puede acceder a __modelo desde la subclase")