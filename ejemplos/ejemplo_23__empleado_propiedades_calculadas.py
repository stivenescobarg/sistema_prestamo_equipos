# ============================================================
# Ejemplo 23: Empleado - Propiedades calculadas
# Descripción: Propiedades que calculan valores dinámicamente.
# ============================================================

class Empleado:
    def __init__(self, nombre, salario_base, horas_extra=0, tarifa_extra=0):
        self._nombre = nombre
        self._salario_base = salario_base
        self._horas_extra = horas_extra
        self._tarifa_extra = tarifa_extra

    @property
    def nombre(self):
        return self._nombre

    @property
    def salario_base(self):
        return self._salario_base

    @salario_base.setter
    def salario_base(self, valor):
        if valor < 0:
            raise ValueError("El salario base no puede ser negativo")
        self._salario_base = valor

    @property
    def horas_extra(self):
        return self._horas_extra

    @horas_extra.setter
    def horas_extra(self, valor):
        if valor < 0:
            raise ValueError("Las horas extra no pueden ser negativas")
        self._horas_extra = valor

    @property
    def tarifa_extra(self):
        return self._tarifa_extra

    @tarifa_extra.setter
    def tarifa_extra(self, valor):
        if valor < 0:
            raise ValueError("La tarifa extra no puede ser negativa")
        self._tarifa_extra = valor

    @property
    def salario_total(self):
        """Calcula el salario total incluyendo las horas extra."""
        return self._salario_base + (self._horas_extra * self._tarifa_extra)


# Crear un empleado
emp = Empleado("Laura Martínez", 2000, 10, 15)

# Acceder a propiedades básicas
print(f"Empleado: {emp.nombre}")
print(f"Salario base: {emp.salario_base}€")
print(f"Horas extra: {emp.horas_extra}")
print(f"Tarifa extra: {emp.tarifa_extra}€/hora")

# Acceder a la propiedad calculada
print(f"Salario total: {emp.salario_total}€")  # 2150€

# Modificar algunos valores
emp.horas_extra = 15
emp.tarifa_extra = 20

# La propiedad calculada se actualiza automáticamente
print(f"Nuevo salario total: {emp.salario_total}€")  # 2300€