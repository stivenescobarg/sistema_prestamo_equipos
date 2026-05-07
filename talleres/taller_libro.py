# ============================================================
# Taller: Clases y Objetos en Python - Clase Libro
# Descripción: Implementación de una clase Libro con atributos
#              y métodos para gestionar información y préstamos.
# ============================================================

class Libro:
    """
    Clase que representa un libro en una biblioteca.
    """
    
    def __init__(self, titulo, autor, paginas):
        """
        Constructor de la clase Libro.
        
        Args:
            titulo (str): El título del libro
            autor (str): El autor del libro
            paginas (int): El número total de páginas
        """
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.disponible = True  # Inicialmente disponible para préstamo
    
    def prestar(self):
        """
        Cambia el estado de disponibilidad a False y devuelve un mensaje.
        
        Returns:
            str: Mensaje indicando el resultado de la operación
        """
        if self.disponible:
            self.disponible = False
            return f"El libro '{self.titulo}' ha sido prestado exitosamente."
        else:
            return f"El libro '{self.titulo}' no está disponible para préstamo (ya está prestado)."
    
    def devolver(self):
        """
        Cambia el estado de disponibilidad a True y devuelve un mensaje.
        
        Returns:
            str: Mensaje indicando el resultado de la operación
        """
        if not self.disponible:
            self.disponible = True
            return f"El libro '{self.titulo}' ha sido devuelto exitosamente."
        else:
            return f"El libro '{self.titulo}' ya estaba disponible en la biblioteca."
    
    def informacion(self):
        """
        Devuelve una cadena con toda la información del libro.
        
        Returns:
            str: Información completa del libro incluyendo su estado
        """
        estado = "Disponible" if self.disponible else "Prestado"
        return f"Título: {self.titulo}\nAutor: {self.autor}\nPáginas: {self.paginas}\nEstado: {estado}"


# ============================================================
# Prueba de la clase Libro
# ============================================================

print("=" * 50)
print("PRUEBA DE LA CLASE LIBRO")
print("=" * 50)

# Crear dos objetos libro diferentes
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 496)
libro2 = Libro("El principito", "Antoine de Saint-Exupéry", 96)
libro3 = Libro("1984", "George Orwell", 328)

print("\n--- LIBROS CREADOS ---")
print("\nLibro 1:")
print(libro1.informacion())
print("\nLibro 2:")
print(libro2.informacion())
print("\nLibro 3:")
print(libro3.informacion())

print("\n" + "=" * 50)
print("PRUEBA DE MÉTODOS")
print("=" * 50)

# Probar método prestar()
print("\n--- PRÉSTAMOS ---")
print(libro1.prestar())
print(libro2.prestar())

# Intentar prestar el mismo libro nuevamente (debe fallar)
print(libro1.prestar())

# Probar método devolver()
print("\n--- DEVOLUCIONES ---")
print(libro1.devolver())

# Intentar devolver un libro que ya está disponible (debe fallar)
print(libro1.devolver())

# Probar devolución del segundo libro
print(libro2.devolver())

print("\n--- ESTADO FINAL DE LOS LIBROS ---")
print("\nLibro 1:")
print(libro1.informacion())
print("\nLibro 2:")
print(libro2.informacion())
print("\nLibro 3:")
print(libro3.informacion())

print("\n" + "=" * 50)
print("FIN DE LA PRUEBA")
print("=" * 50)