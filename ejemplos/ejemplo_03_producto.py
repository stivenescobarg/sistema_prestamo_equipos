# ejemplo_03_producto.py
# Tema: Constructor con valores predeterminados
# Fuente: Concepto teórico de clase y objeto - Clase y constructor

class Producto:
    """Clase que modela un producto con nombre, precio y stock opcional."""

    def __init__(self, nombre, precio, stock=0):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock  # Valor predeterminado: 0

# Creamos productos con y sin especificar el stock
laptop = Producto("Laptop XPS", 1200)           # stock será 0 (por defecto)
teclado = Producto("Teclado mecánico", 80, 15)  # stock será 15

print("=== Ejemplo 03: Clase Producto con valores predeterminados ===")
print(f"Producto: {laptop.nombre}")
print(f"  Precio: ${laptop.precio}")
print(f"  Stock: {laptop.stock} unidades (valor por defecto)")

print(f"\nProducto: {teclado.nombre}")
print(f"  Precio: ${teclado.precio}")
print(f"  Stock: {teclado.stock} unidades")