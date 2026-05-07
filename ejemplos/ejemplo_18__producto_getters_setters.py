# ============================================================
# Ejemplo 18: Producto - Getters y Setters completos
# Descripción: Clase Producto con control de acceso a atributos.
# ============================================================

class Producto:
    def __init__(self, nombre, precio, stock=0):
        self._nombre = nombre
        self._precio = precio
        self._stock = stock
        self._descuento = 0

    # Getters
    def get_nombre(self):
        return self._nombre

    def get_precio(self):
        # Aplicamos el descuento al devolver el precio
        return self._precio * (1 - self._descuento)

    def get_precio_base(self):
        # Devolvemos el precio sin descuento
        return self._precio

    def get_stock(self):
        return self._stock

    def get_descuento(self):
        return self._descuento

    # Setters
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


# Crear un producto
laptop = Producto("Laptop XPS", 1200.0, 10)

# Obtener información
print(f"Producto: {laptop.get_nombre()}")
print(f"Precio base: ${laptop.get_precio_base()}")
print(f"Stock disponible: {laptop.get_stock()} unidades")

# Aplicar un descuento del 15%
laptop.set_descuento(0.15)
print(f"Precio con descuento: ${laptop.get_precio()}")

# Actualizar el stock después de una venta
laptop.set_stock(laptop.get_stock() - 1)
print(f"Stock actualizado: {laptop.get_stock()} unidades")

# Intentar establecer un precio negativo
try:
    laptop.set_precio(-100)
except ValueError as e:
    print(f"Error: {e}")  # Error: El precio debe ser un número positivo