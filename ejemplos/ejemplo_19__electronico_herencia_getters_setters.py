# ============================================================
# Ejemplo 19: Electrónico - Herencia con getters y setters
# Descripción: Subclase que extiende Producto con más atributos.
# ============================================================

class Producto:
    def __init__(self, nombre, precio, stock=0):
        self._nombre = nombre
        self._precio = precio
        self._stock = stock
        self._descuento = 0

    def get_nombre(self):
        return self._nombre

    def get_precio(self):
        return self._precio * (1 - self._descuento)

    def get_precio_base(self):
        return self._precio

    def get_stock(self):
        return self._stock

    def get_descuento(self):
        return self._descuento

    def set_nombre(self, nuevo_nombre):
        if not isinstance(nuevo_nombre, str) or len(nuevo_nombre) == 0:
            raise ValueError("El nombre debe ser una cadena no vacía")
        self._nombre = nuevo_nombre

    def set_precio(self, nuevo_precio):
        if not isinstance(nuevo_precio, (int, float)) or nuevo_precio < 0:
            raise ValueError("El precio debe ser un número positivo")
        self._precio = nuevo_precio

    def set_stock(self, nuevo_stock):
        if not isinstance(nuevo_stock, int) or nuevo_stock < 0:
            raise ValueError("El stock debe ser un entero positivo")
        self._stock = nuevo_stock

    def set_descuento(self, nuevo_descuento):
        if not isinstance(nuevo_descuento, float) or not 0 <= nuevo_descuento <= 1:
            raise ValueError("El descuento debe ser un número entre 0 y 1")
        self._descuento = nuevo_descuento


class Electronico(Producto):
    def __init__(self, nombre, precio, stock, garantia_meses):
        super().__init__(nombre, precio, stock)
        self._garantia_meses = garantia_meses
        self._activado = False

    # Getters adicionales
    def get_garantia_meses(self):
        return self._garantia_meses

    def esta_activado(self):
        return self._activado

    # Setters adicionales
    def set_garantia_meses(self, meses):
        if not isinstance(meses, int) or meses < 0:
            raise ValueError("Los meses de garantía deben ser un entero positivo")
        self._garantia_meses = meses

    def activar(self):
        self._activado = True

    def desactivar(self):
        self._activado = False

    # Sobrescribir el setter de precio para añadir lógica adicional
    def set_precio(self, nuevo_precio):
        # Llamamos al setter de la clase padre
        super().set_precio(nuevo_precio)
        # Lógica adicional específica para productos electrónicos
        if nuevo_precio > 1000:
            # Productos caros tienen garantía extendida automáticamente
            self._garantia_meses = max(self._garantia_meses, 24)