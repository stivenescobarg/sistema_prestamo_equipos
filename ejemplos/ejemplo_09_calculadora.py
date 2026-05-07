# ejemplo_09_calculadora.py
# Tema: Métodos con parámetros y retorno de valores
# Fuente: Concepto teórico de clase y objeto - Métodos

class Calculadora:
    """Clase que modela una calculadora con operaciones básicas y estadísticas."""

    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            return "Error: División por cero"
        return a / b

    def calcular_estadisticas(self, numeros):
        """Devuelve un diccionario con estadísticas de una lista de números."""
        if not numeros:
            return {"suma": 0, "promedio": 0, "minimo": None, "maximo": None}

        return {
            "suma": sum(numeros),
            "promedio": sum(numeros) / len(numeros),
            "minimo": min(numeros),
            "maximo": max(numeros)
        }


# Uso de la clase
print("=== Ejemplo 09: Calculadora con métodos ===")
calc = Calculadora()

print(f"5 + 3 = {calc.sumar(5, 3)}")
print(f"10 - 4 = {calc.restar(10, 4)}")
print(f"6 x 7 = {calc.multiplicar(6, 7)}")
print(f"10 / 2 = {calc.dividir(10, 2)}")
print(f"10 / 0 = {calc.dividir(10, 0)}")

print("\n-- Estadísticas de una lista --")
datos = [4, 7, 2, 9, 5]
estadisticas = calc.calcular_estadisticas(datos)
print(f"Datos: {datos}")
print(f"Suma: {estadisticas['suma']}")
print(f"Promedio: {estadisticas['promedio']}")
print(f"Mínimo: {estadisticas['minimo']}")
print(f"Máximo: {estadisticas['maximo']}")