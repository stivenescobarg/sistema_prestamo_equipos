# ejemplo_02_persona.py
# Tema: Constructor __init__ y atributos de instancia
# Fuente: Concepto teórico de clase y objeto - Clase y constructor

class Persona:
    """Clase que modela una persona con nombre y edad."""

    def __init__(self, nombre, edad):
        # self.nombre y self.edad son atributos de instancia
        self.nombre = nombre
        self.edad = edad

# Creamos dos objetos Persona con distintos valores
ana = Persona("Ana García", 28)
juan = Persona("Juan López", 35)

print("=== Ejemplo 02: Clase Persona con constructor ===")
print(f"Nombre de ana: {ana.nombre}")
print(f"Edad de ana: {ana.edad}")
print(f"Nombre de juan: {juan.nombre}")
print(f"Edad de juan: {juan.edad}")

# Comprobamos que cada objeto tiene sus propios valores
ana.edad = 29  # Modificamos solo a ana
print(f"\nDespués de cumpleaños de ana:")
print(f"Edad de ana: {ana.edad}")
print(f"Edad de juan (no cambia): {juan.edad}")