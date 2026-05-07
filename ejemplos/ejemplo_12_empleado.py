# ejemplo_12_empleado.py
# Tema: Métodos de clase (@classmethod) y estáticos (@staticmethod)
# Fuente: Concepto teórico de clase y objeto - Métodos

class Empleado:
    """Clase que demuestra @classmethod y @staticmethod."""

    # Atributo de clase: cuenta el número total de empleados creados
    num_empleados = 0

    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
        Empleado.num_empleados += 1  # Incrementamos el contador de clase

    @classmethod
    def desde_salario_anual(cls, nombre, salario_anual):
        """Constructor alternativo: recibe salario anual y lo convierte a mensual."""
        salario_mensual = salario_anual / 12
        return cls(nombre, salario_mensual)

    @classmethod
    def obtener_total_empleados(cls):
        """Devuelve el total de empleados creados."""
        return cls.num_empleados

    @staticmethod
    def es_salario_valido(salario):
        """Método estático: valida si un salario es positivo (no necesita self ni cls)."""
        return isinstance(salario, (int, float)) and salario > 0

    def __str__(self):
        return f"Empleado: {self.nombre} | Salario mensual: ${self.salario:,.2f}"


# Uso de la clase
print("=== Ejemplo 12: Métodos estáticos y de clase en Empleado ===")

emp1 = Empleado("Ana", 3000)
emp2 = Empleado.desde_salario_anual("Carlos", 48000)  # 48000/12 = 4000

print(emp1)
print(emp2)
print(f"\nTotal empleados: {Empleado.obtener_total_empleados()}")

print("\n-- Método estático: validar salario --")
print(f"¿Es válido 3000? {Empleado.es_salario_valido(3000)}")
print(f"¿Es válido -500? {Empleado.es_salario_valido(-500)}")
print(f"¿Es válido 'mil'? {Empleado.es_salario_valido('mil')}")