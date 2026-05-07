# ============================================================
# Ejemplo 14: CuentaBancaria - Atributos privados con doble guion bajo
# Descripción: Ejemplo de name mangling en Python.
# ============================================================

class CuentaBancaria:
    def __init__(self, titular, saldo_inicial, pin):
        self._titular = titular
        self._saldo = saldo_inicial
        self.__pin = pin  # Atributo "realmente" privado

    def validar_pin(self, pin_ingresado):
        return self.__pin == pin_ingresado


cuenta = CuentaBancaria("Ana García", 1000, "1234")

# Esto generará un AttributeError
try:
    print(cuenta.__pin)
except AttributeError as e:
    print(f"Error: {e}")

# Esto funciona, pero requiere conocer el mecanismo interno
print(cuenta._CuentaBancaria__pin)  # Imprime: 1234