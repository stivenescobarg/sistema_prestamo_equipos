# ============================================================
# Ejemplo 24: Producto - Migración de getters/setters a propiedades
# Descripción: Versión final con propiedades.
# ============================================================

class ProductoV3:
    def __init__(self, nombre, precio):
        self._nombre = nombre
        self._precio = precio

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        if valor < 0:
            raise ValueError("El precio no puede ser negativo")
        self._precio = valor