# ============================================================
# Ejemplo 15: Producto - Validación de datos con atributos privados
# Descripción: Validación antes de asignar atributos.
# ============================================================

class Producto:
    def __init__(self, nombre, precio):
        self._nombre = nombre
        # Validamos el precio antes de asignarlo
        if precio < 0:
            raise ValueError("El precio no puede ser negativo")
        self._precio = precio