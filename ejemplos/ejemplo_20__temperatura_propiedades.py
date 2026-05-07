# ============================================================
# Ejemplo 20: Temperatura - Propiedades con @property
# Descripción: Uso de propiedades para encapsulación elegante.
# ============================================================

class Temperatura:
    def __init__(self, celsius=0):
        self._celsius = celsius

    @property
    def celsius(self):
        """Obtiene la temperatura en grados Celsius."""
        return self._celsius

    @celsius.setter
    def celsius(self, valor):
        """Establece la temperatura en grados Celsius."""
        if valor < -273.15:
            raise ValueError("La temperatura no puede ser menor que el cero absoluto")
        self._celsius = valor

    @property
    def fahrenheit(self):
        """Obtiene la temperatura en grados Fahrenheit."""
        return self._celsius * 9/5 + 32

    @fahrenheit.setter
    def fahrenheit(self, valor):
        """Establece la temperatura en grados Fahrenheit."""
        celsius = (valor - 32) * 5/9
        if celsius < -273.15:
            raise ValueError("La temperatura no puede ser menor que el cero absoluto")
        self._celsius = celsius


# Crear un objeto temperatura
temp = Temperatura(25)

# Acceder a las propiedades como si fueran atributos
print(f"Temperatura: {temp.celsius}°C")  # 25°C
print(f"Temperatura: {temp.fahrenheit}°F")  # 77°F

# Modificar las propiedades
temp.celsius = 30
print(f"Nueva temperatura: {temp.celsius}°C")  # 30°C
print(f"Nueva temperatura: {temp.fahrenheit}°F")  # 86°F

# Modificar usando fahrenheit
temp.fahrenheit = 68
print(f"Temperatura actualizada: {temp.celsius}°C")  # 20°C

# Intentar establecer una temperatura imposible
try:
    temp.celsius = -300
except ValueError as e:
    print(f"Error: {e}")  # Error: La temperatura no puede ser menor que el cero absoluto