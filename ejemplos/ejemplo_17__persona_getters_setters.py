# ============================================================
# Ejemplo 17: Persona - Getters y Setters
# Descripción: Uso de métodos get y set para encapsulación.
# ============================================================

class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    # Getter para nombre
    def get_nombre(self):
        return self._nombre

    # Setter para nombre
    def set_nombre(self, nuevo_nombre):
        if isinstance(nuevo_nombre, str) and len(nuevo_nombre) > 0:
            self._nombre = nuevo_nombre
        else:
            raise ValueError("El nombre debe ser una cadena no vacía")

    # Getter para edad
    def get_edad(self):
        return self._edad

    # Setter para edad
    def set_edad(self, nueva_edad):
        if isinstance(nueva_edad, int) and 0 <= nueva_edad <= 120:
            self._edad = nueva_edad
        else:
            raise ValueError("La edad debe ser un entero entre 0 y 120")


# Crear una instancia
ana = Persona("Ana López", 29)

# Usar getters para acceder a los datos
print(ana.get_nombre())  # Ana López
print(ana.get_edad())    # 29

# Usar setters para modificar los datos
ana.set_nombre("Ana María López")
ana.set_edad(30)

# Verificar los cambios
print(ana.get_nombre())  # Ana María López
print(ana.get_edad())    # 30

# Intentar asignar un valor inválido
try:
    ana.set_edad(-5)
except ValueError as e:
    print(f"Error: {e}")  # Error: La edad debe ser un entero entre 0 y 120