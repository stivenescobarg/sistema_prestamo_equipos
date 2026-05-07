# ejemplo_01_coche.py
# Tema: Definición básica de una clase en Python
# Fuente: Concepto teórico de clase y objeto

class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = 0
        self.encendido = False
        self.velocidad_maxima = 200

    def encender(self):
        if not self.encendido:
            self.encendido = True
            return f"{self.marca} {self.modelo} encendido."
        return f"{self.marca} {self.modelo} ya estaba encendido."

    def apagar(self):
        if self.encendido:
            self.encendido = False
            self.velocidad = 0
            return f"{self.marca} {self.modelo} apagado."
        return f"{self.marca} {self.modelo} ya estaba apagado."

    def acelerar(self, incremento):
        if not self.encendido:
            return f"No se puede acelerar: {self.marca} {self.modelo} esta apagado."
        nueva_velocidad = self.velocidad + incremento
        if nueva_velocidad > self.velocidad_maxima:
            self.velocidad = self.velocidad_maxima
            return f"Velocidad maxima alcanzada: {self.velocidad} km/h"
        self.velocidad = nueva_velocidad
        return f"Velocidad actual: {self.velocidad} km/h"

    def frenar(self, decremento):
        if self.velocidad == 0:
            return "El coche ya esta detenido."
        nueva_velocidad = self.velocidad - decremento
        if nueva_velocidad < 0:
            self.velocidad = 0
            return "Coche detenido."
        self.velocidad = nueva_velocidad
        return f"Velocidad actual: {self.velocidad} km/h"


# Programa principal
mi_coche = Coche("Renault", "Corolla")

print(mi_coche.encender())
print(mi_coche.encender())      # Ya estaba encendido
print(mi_coche.acelerar(30))
print(mi_coche.acelerar(40))
print(mi_coche.frenar(20))
print(mi_coche.frenar(100))    # Queda en 0
print(mi_coche.apagar())
print(mi_coche.acelerar(10))   # No puede, esta apagado