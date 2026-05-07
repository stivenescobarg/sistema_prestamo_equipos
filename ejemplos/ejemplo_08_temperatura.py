# ejemplo_08_temperatura.py
# Tema: Propiedades con @property, getter y setter
# Fuente: Concepto teórico de clase y objeto - Atributos / Encapsulación - Propiedades

class Temperatura:
    """Clase que demuestra el uso de propiedades para conversión Celsius/Fahrenheit."""

    def __init__(self, celsius=0):
        self._celsius = celsius  # Atributo privado (convención _)

    @property
    def celsius(self):
        """Getter: obtiene la temperatura en Celsius."""
        return self._celsius

    @celsius.setter
    def celsius(self, valor):
        """Setter: valida y asigna la temperatura en Celsius."""
        if valor < -273.15:
            raise ValueError("La temperatura no puede ser menor que el cero absoluto")
        self._celsius = valor

    @property
    def fahrenheit(self):
        """Getter: calcula y devuelve la temperatura en Fahrenheit."""
        return self._celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, valor):
        """Setter: convierte de Fahrenheit a Celsius y asigna."""
        self.celsius = (valor - 32) * 5 / 9  # Reutiliza la validación del setter celsius


# Uso de la clase
print("=== Ejemplo 08: Clase Temperatura con propiedades ===")
temp = Temperatura(25)

print(f"Temperatura: {temp.celsius}°C = {temp.fahrenheit}°F")

temp.celsius = 100
print(f"Temperatura: {temp.celsius}°C = {temp.fahrenheit}°F")

temp.fahrenheit = 32
print(f"Temperatura: {temp.celsius}°C = {temp.fahrenheit}°F")

# Validación automática
try:
    temp.celsius = -300
except ValueError as e:
    print(f"\nError de validación: {e}")