# ============================================================
# Taller de Encapsulación - Clase CuentaBancaria
# Descripción: Implementación de una clase con atributos privados
#              y propiedades para encapsular datos.
# ============================================================

class CuentaBancaria:
    """
    Clase que representa una cuenta bancaria con encapsulación.
    Los atributos son privados y se accede mediante propiedades.
    """
    
    def __init__(self, titular, saldo_inicial=0.0):
        """
        Constructor de la clase CuentaBancaria.
        
        Args:
            titular (str): Nombre del titular de la cuenta (solo lectura)
            saldo_inicial (float): Saldo inicial de la cuenta (por defecto 0)
        """
        self._titular = titular
        self._saldo = saldo_inicial
    
    # Propiedad titular - solo lectura (sin setter)
    @property
    def titular(self):
        """
        Propiedad de solo lectura para obtener el titular.
        
        Returns:
            str: Nombre del titular de la cuenta
        """
        return self._titular
    
    # Propiedad saldo - con validación en el setter
    @property
    def saldo(self):
        """
        Propiedad para obtener el saldo actual.
        
        Returns:
            float: Saldo actual de la cuenta
        """
        return self._saldo
    
    @saldo.setter
    def saldo(self, nuevo_saldo):
        """
        Setter para modificar el saldo con validación.
        
        Args:
            nuevo_saldo (float): Nuevo saldo a establecer
            
        Raises:
            ValueError: Si el nuevo saldo es negativo
        """
        if nuevo_saldo < 0:
            raise ValueError("El saldo no puede ser negativo")
        self._saldo = nuevo_saldo
    
    def depositar(self, cantidad):
        """
        Incrementa el saldo si la cantidad es positiva.
        
        Args:
            cantidad (float): Cantidad a depositar
            
        Returns:
            bool: True si el depósito fue exitoso, False en caso contrario
        """
        if cantidad > 0:
            self._saldo += cantidad
            return True
        return False
    
    def retirar(self, cantidad):
        """
        Disminuye el saldo si hay suficiente dinero.
        
        Args:
            cantidad (float): Cantidad a retirar
            
        Returns:
            bool: True si el retiro fue exitoso, False en caso contrario
        """
        if cantidad > 0 and self._saldo >= cantidad:
            self._saldo -= cantidad
            return True
        return False
    
    def __str__(self):
        """
        Representación en string de la cuenta bancaria.
        
        Returns:
            str: Información de la cuenta
        """
        return f"Cuenta de {self._titular} - Saldo: ${self._saldo:.2f}"


# ============================================================
# Prueba de la clase CuentaBancaria
# ============================================================

print("=" * 60)
print("TALLER DE ENCAPSULACIÓN - PRUEBA DE CUENTABANCARIA")
print("=" * 60)

# Crear cuentas bancarias
print("\n--- CREANDO CUENTAS ---")
cuenta1 = CuentaBancaria("Ana García", 1000.00)
cuenta2 = CuentaBancaria("Carlos López")  # Saldo inicial por defecto 0
cuenta3 = CuentaBancaria("María Rodríguez", 500.50)

print(f"Cuenta 1: {cuenta1}")
print(f"Cuenta 2: {cuenta2}")
print(f"Cuenta 3: {cuenta3}")

# Probar propiedad titular (solo lectura)
print("\n--- PROPIEDAD TITULAR (SOLO LECTURA) ---")
print(f"Titular cuenta 1: {cuenta1.titular}")
print(f"Titular cuenta 2: {cuenta2.titular}")
print(f"Titular cuenta 3: {cuenta3.titular}")

# Intentar modificar el titular (debe fallar porque es solo lectura)
print("\n--- INTENTANDO MODIFICAR TITULAR (DEBE FALLAR) ---")
try:
    cuenta1.titular = "Nuevo Nombre"
except AttributeError as e:
    print(f"Error (correcto): No se puede modificar el titular - {e}")

# Probar propiedad saldo (lectura y escritura con validación)
print("\n--- PROPIEDAD SALDO ---")
print(f"Saldo cuenta 1: ${cuenta1.saldo:.2f}")
print(f"Saldo cuenta 2: ${cuenta2.saldo:.2f}")
print(f"Saldo cuenta 3: ${cuenta3.saldo:.2f}")

# Probar setter de saldo con valores válidos
print("\n--- MODIFICANDO SALDO DIRECTAMENTE (VÁLIDO) ---")
cuenta2.saldo = 250.00
print(f"Nuevo saldo cuenta 2: ${cuenta2.saldo:.2f}")

# Probar setter de saldo con valor negativo (debe lanzar ValueError)
print("\n--- INTENTANDO ESTABLECER SALDO NEGATIVO (DEBE FALLAR) ---")
try:
    cuenta2.saldo = -100.00
except ValueError as e:
    print(f"Error (correcto): {e}")

# Probar método depositar
print("\n--- MÉTODO DEPOSITAR ---")
print(f"Cuenta 1 antes del depósito: ${cuenta1.saldo:.2f}")
resultado1 = cuenta1.depositar(200.00)
print(f"Depositar $200.00: {'Exitoso' if resultado1 else 'Fallido'}")
print(f"Cuenta 1 después del depósito: ${cuenta1.saldo:.2f}")

# Intentar depositar cantidad negativa
resultado2 = cuenta1.depositar(-50.00)
print(f"\nIntentar depositar -$50.00: {'Exitoso' if resultado2 else 'Fallido'} (debe fallar)")

# Probar método retirar
print("\n--- MÉTODO RETIRAR ---")
print(f"Cuenta 1 antes del retiro: ${cuenta1.saldo:.2f}")
resultado3 = cuenta1.retirar(100.00)
print(f"Retirar $100.00: {'Exitoso' if resultado3 else 'Fallido'}")
print(f"Cuenta 1 después del retiro: ${cuenta1.saldo:.2f}")

# Intentar retirar más dinero del que hay
print(f"\nCuenta 2 saldo actual: ${cuenta2.saldo:.2f}")
resultado4 = cuenta2.retirar(1000.00)
print(f"Intentar retirar $1000.00: {'Exitoso' if resultado4 else 'Fallido'} (debe fallar por saldo insuficiente)")

# Intentar retirar cantidad negativa
resultado5 = cuenta2.retirar(-30.00)
print(f"Intentar retirar -$30.00: {'Exitoso' if resultado5 else 'Fallido'} (debe fallar)")

# Probar múltiples operaciones
print("\n--- MÚLTIPLES OPERACIONES ---")
print(f"Cuenta 3 inicial: {cuenta3}")

# Depositar varias veces
cuenta3.depositar(100.00)
cuenta3.depositar(50.00)
cuenta3.depositar(25.00)
print(f"Después de depositar $100, $50 y $25: {cuenta3}")

# Retirar varias veces
cuenta3.retirar(75.00)
cuenta3.retirar(30.00)
print(f"Después de retirar $75 y $30: {cuenta3}")

# Verificar saldo final
print(f"\n--- SALDOS FINALES ---")
print(f"Cuenta 1: {cuenta1}")
print(f"Cuenta 2: {cuenta2}")
print(f"Cuenta 3: {cuenta3}")

print("\n" + "=" * 60)
print("FIN DEL TALLER DE ENCAPSULACIÓN")
print("=" * 60)