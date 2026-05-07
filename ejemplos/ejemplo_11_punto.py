# ejemplo_11_punto.py
# Tema: Métodos especiales (dunder methods)
# Fuente: Concepto teórico de clase y objeto - Métodos

class Punto:
    """Clase que demuestra métodos especiales como __str__, __repr__, __add__, __eq__."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        """Representación técnica del objeto (para desarrolladores)."""
        return f"Punto({self.x}, {self.y})"

    def __str__(self):
        """Representación legible del objeto (para usuarios)."""
        return f"({self.x}, {self.y})"

    def __add__(self, otro):
        """Soporte para el operador +."""
        return Punto(self.x + otro.x, self.y + otro.y)

    def __eq__(self, otro):
        """Soporte para el operador ==."""
        if not isinstance(otro, Punto):
            return False
        return self.x == otro.x and self.y == otro.y

    def __len__(self):
        """Soporte para len() — distancia Manhattan desde el origen."""
        return abs(self.x) + abs(self.y)


# Uso de la clase
print("=== Ejemplo 11: Métodos especiales en Clase Punto ===")
p1 = Punto(3, 4)
p2 = Punto(1, 2)

print(f"str(p1):    {p1}")          # Usa __str__
print(f"repr(p1):   {repr(p1)}")   # Usa __repr__

p3 = p1 + p2
print(f"p1 + p2 = {p3}")           # Usa __add__

print(f"p1 == p2: {p1 == p2}")     # Usa __eq__
print(f"p1 == Punto(3,4): {p1 == Punto(3, 4)}")

print(f"len(p1): {len(p1)}")       # Usa __len__ (distancia Manhattan)