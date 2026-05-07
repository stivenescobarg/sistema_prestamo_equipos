# ejemplo_06_libro.py
# Tema: Clase completa con atributos y métodos de comportamiento
# Fuente: Concepto teórico de clase y objeto - Métodos

class Libro:
    """Clase que modela un libro con seguimiento de lectura."""

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.pagina_actual = 0
        self.abierto = False

    def abrir(self):
        if self.abierto:
            return f"{self.titulo} ya está abierto"
        self.abierto = True
        return f"{self.titulo} ha sido abierto"

    def cerrar(self):
        if not self.abierto:
            return f"{self.titulo} ya está cerrado"
        self.abierto = False
        return f"{self.titulo} ha sido cerrado"

    def leer(self, num_paginas):
        if not self.abierto:
            return f"No puedes leer: {self.titulo} está cerrado"

        if self.pagina_actual >= self.paginas:
            return f"Ya has terminado de leer {self.titulo}"

        paginas_restantes = self.paginas - self.pagina_actual
        paginas_a_leer = min(num_paginas, paginas_restantes)
        self.pagina_actual += paginas_a_leer

        if self.pagina_actual >= self.paginas:
            return f"Has leído {paginas_a_leer} páginas y has terminado {self.titulo}"

        return f"Has leído {paginas_a_leer} páginas. Estás en la página {self.pagina_actual} de {self.paginas}"

    def reiniciar_lectura(self):
        self.pagina_actual = 0
        return f"Has reiniciado la lectura de {self.titulo}"

    def __str__(self):
        estado = "abierto" if self.abierto else "cerrado"
        progreso = f"{self.pagina_actual}/{self.paginas} páginas"
        return f"{self.titulo} por {self.autor} - {progreso} - {estado}"


# Uso de la clase
print("=== Ejemplo 06: Clase Libro con métodos ===")
libro = Libro("El Quijote", "Miguel de Cervantes", 863)

print(libro.leer(50))       # No se puede leer si está cerrado
print(libro.abrir())
print(libro.leer(50))
print(libro.leer(100))
print(libro.cerrar())
print(libro.abrir())
print(libro.leer(713))
print(libro.reiniciar_lectura())
print(libro)                # Usa __str__