# ============================================================
# Ejemplo 21: Persona - Propiedades con getter, setter y deleter
# Descripción: Demostración completa de propiedades.
# ============================================================

class Persona:
    def __init__(self, nombre):
        self._nombre = nombre
        self._amigos = []

    @property
    def nombre(self):
        """Obtiene el nombre de la persona."""
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        """Establece el nombre de la persona."""
        if not isinstance(valor, str) or not valor:
            raise ValueError("El nombre debe ser una cadena no vacía")
        self._nombre = valor

    @property
    def amigos(self):
        """Obtiene la lista de amigos (como copia para evitar modificaciones directas)."""
        return self._amigos.copy()

    @amigos.deleter
    def amigos(self):
        """Elimina todos los amigos."""
        self._amigos = []
        print("Lista de amigos eliminada")


# Crear una persona
p = Persona("Carlos")

# Usar el getter
print(p.nombre)  # Carlos

# Usar el setter
p.nombre = "Carlos Rodríguez"
print(p.nombre)  # Carlos Rodríguez

# Intentar modificar la lista de amigos directamente (no afecta al original)
amigos = p.amigos
amigos.append("Ana")
print(p.amigos)  # [] - La lista original no se modificó

# Usar el deleter
del p.amigos