# ============================================================
# Ejemplo 22: Círculo - Propiedades de solo lectura
# Descripción: Uso de propiedades sin setter para solo lectura.
# ============================================================

class Circulo:
    def __init__(self, radio):
        self._radio = radio

    @property
    def radio(self):
        return self._radio

    @radio.setter
    def radio(self, valor):
        if valor <= 0:
            raise ValueError("El radio debe ser positivo")
        self._radio = valor

    @property
    def area(self):
        """Área del círculo (propiedad de solo lectura)."""
        import math
        return math.pi * self._radio ** 2

    @property
    def perimetro(self):
        """Perímetro del círculo (propiedad de solo lectura)."""
        import math
        return 2 * math.pi * self._radio


c = Circulo(5)
print(f"Radio: {c.radio}")  # 5
print(f"Área: {c.area:.2f}")  # 78.54
print(f"Perímetro: {c.perimetro:.2f}")  # 31.42

# Podemos cambiar el radio
c.radio = 10
print(f"Nuevo radio: {c.radio}")  # 10
print(f"Nueva área: {c.area:.2f}")  # 314.16

# Pero no podemos cambiar el área directamente
try:
    c.area = 100
except AttributeError as e:
    print(f"Error: {e}")  # Error: can't set attribute 'area'