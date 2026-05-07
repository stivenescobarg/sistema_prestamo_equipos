# ejemplo_10_fecha.py
# Tema: Métodos de clase (@classmethod) como constructores alternativos
# Fuente: Concepto teórico de clase y objeto - Clase y constructor

class Fecha:
    """Clase que demuestra el uso de @classmethod para constructores alternativos."""

    def __init__(self, dia, mes, año):
        self.dia = dia
        self.mes = mes
        self.año = año

    @classmethod
    def desde_texto(cls, texto):
        """Constructor alternativo: crea una Fecha desde un string 'DD-MM-AAAA'."""
        dia, mes, año = map(int, texto.split('-'))
        return cls(dia, mes, año)

    @classmethod
    def hoy(cls):
        """Constructor alternativo: crea una Fecha con la fecha actual del sistema."""
        import datetime
        fecha_actual = datetime.date.today()
        return cls(fecha_actual.day, fecha_actual.month, fecha_actual.year)

    def __str__(self):
        return f"{self.dia:02d}/{self.mes:02d}/{self.año}"


# Uso de la clase
print("=== Ejemplo 10: Clase Fecha con constructores alternativos ===")

# Constructor normal
fecha1 = Fecha(15, 3, 2023)
print(f"Constructor normal:    {fecha1}")

# Constructor desde texto
fecha2 = Fecha.desde_texto("25-12-2024")
print(f"Constructor desde txt: {fecha2}")

# Constructor con fecha de hoy
fecha3 = Fecha.hoy()
print(f"Constructor hoy:       {fecha3}")