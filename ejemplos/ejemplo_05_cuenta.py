# ejemplo_05_cuenta.py
# Tema: Constructor con validación de datos
# Fuente: Concepto teórico de clase y objeto - Clase y constructor

class Cuenta:
    """Clase que modela una cuenta bancaria básica con validación de saldo inicial."""

    def __init__(self, titular, saldo_inicial):
        self.titular = titular

        # Validamos que el saldo inicial no sea negativo
        if saldo_inicial < 0:
            raise ValueError("El saldo inicial no puede ser negativo")

        self.saldo = saldo_inicial

# Cuenta válida
print("=== Ejemplo 05: Clase Cuenta con validación en el constructor ===")
cuenta_ana = Cuenta("Ana García", 1000)
print(f"Cuenta creada para: {cuenta_ana.titular}")
print(f"Saldo inicial: ${cuenta_ana.saldo}")

# Cuenta con saldo inválido
try:
    cuenta_problematica = Cuenta("Juan López", -500)
except ValueError as e:
    print(f"\nError al crear cuenta con saldo negativo: {e}")