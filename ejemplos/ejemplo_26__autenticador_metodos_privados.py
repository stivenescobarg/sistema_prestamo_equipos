# ============================================================
# Ejemplo 26: Autenticador - Métodos privados
# Descripción: Uso de métodos privados con __.
# ============================================================

class Autenticador:
    def __init__(self, usuario, contrasena):
        self._usuario = usuario
        self._contrasena_hash = self.__generar_hash(contrasena)

    def __generar_hash(self, contrasena):
        """Método privado para generar un hash de la contraseña."""
        import hashlib
        return hashlib.sha256(contrasena.encode()).hexdigest()

    def verificar_contrasena(self, contrasena_ingresada):
        """Método público que utiliza el método privado internamente."""
        hash_ingresado = self.__generar_hash(contrasena_ingresada)
        return hash_ingresado == self._contrasena_hash