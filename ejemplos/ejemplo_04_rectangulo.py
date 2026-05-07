# ejemplo_04_rectangulo.py
# Tema: Constructor con cálculos iniciales
# Fuente: Concepto teórico de clase y objeto - Clase y constructor

class Rectangulo:
    """Clase que modela un rectángulo y calcula área y perímetro al crearse."""

    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        # El constructor también puede realizar cálculos al inicializar
        self.area = ancho * alto
        self.perimetro = 2 * (ancho + alto)

# Creamos un rectángulo
rect = Rectangulo(5, 3)

print("=== Ejemplo 04: Clase Rectángulo con cálculos en el constructor ===")
print(f"Dimensiones: {rect.ancho} x {rect.alto}")
print(f"Área: {rect.area}")
print(f"Perímetro: {rect.perimetro}")

# Otro rectángulo
rect2 = Rectangulo(10, 4)
print(f"\nDimensiones: {rect2.ancho} x {rect2.alto}")
print(f"Área: {rect2.area}")
print(f"Perímetro: {rect2.perimetro}")