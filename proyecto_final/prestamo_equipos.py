# =============================================================================
# SISTEMA DE PRÉSTAMOS DE EQUIPOS

from datetime import date


# =============================================================================
# CLASE: Equipo
# Representa un equipo físico del inventario institucional.
# Encapsula: nombre, disponibilidad e historial de préstamos.
# =============================================================================

class Equipo:
    """
    Modela un equipo del inventario con control de disponibilidad
    e historial de préstamos.
    """

    def __init__(self, nombre):
        # Atributos privados — protegidos con doble guion bajo
        self.__nombre = nombre
        self.__disponible = True          # True = disponible para préstamo
        self.__historial = []             # Lista de tuplas (usuario, fecha)

    # -------------------------------------------------------------------------
    # Propiedades (getters con @property)
    # -------------------------------------------------------------------------

    @property
    def nombre(self):
        """Retorna el nombre del equipo."""
        return self.__nombre

    @property
    def disponible(self):
        """Retorna True si el equipo está disponible."""
        return self.__disponible

    @property
    def historial(self):
        """
        Retorna una copia del historial de préstamos.
        Se devuelve copia para proteger la lista interna.
        """
        return self.__historial.copy()

    @property
    def estado(self):
        """Retorna el estado del equipo como texto legible."""
        return "Disponible" if self.__disponible else "Prestado"

    # -------------------------------------------------------------------------
    # Métodos públicos
    # -------------------------------------------------------------------------

    def registrar_prestamo(self, usuario):
        """
        Registra un préstamo del equipo a un usuario.
        Guarda el préstamo como tupla inmutable (usuario, fecha).
        Retorna True si se realizó con éxito, False si ya estaba prestado.
        """
        if not self.__disponible:
            return False

        fecha_hoy = date.today().strftime("%d/%m/%Y")
        registro = (usuario, fecha_hoy)        # Tupla inmutable
        self.__historial.append(registro)
        self.__disponible = False
        return True

    def registrar_devolucion(self):
        """
        Marca el equipo como disponible nuevamente.
        Retorna True si se realizó con éxito, False si ya estaba disponible.
        """
        if self.__disponible:
            return False
        self.__disponible = True
        return True

    def tiene_historial(self):
        """Retorna True si el equipo tiene al menos un préstamo registrado."""
        return len(self.__historial) > 0

    def ultimo_prestamo(self):
        """Retorna la tupla del último préstamo o None si no hay historial."""
        if not self.__historial:
            return None
        return self.__historial[-1]

    def __str__(self):
        return f"{self.__nombre} [{self.estado}]"

    def __repr__(self):
        return f"Equipo(nombre='{self.__nombre}', disponible={self.__disponible})"


# =============================================================================
# CLASE: Usuario
# Representa a una persona que puede solicitar préstamos de equipos.
# Encapsula: nombre, identificación y lista de préstamos activos.
# =============================================================================

class Usuario:
    """
    Modela un usuario del sistema con validación de nombre e identificación.
    Lleva control de cuántos préstamos activos tiene.
    """

    # Atributo de clase: límite máximo de préstamos simultáneos por usuario
    LIMITE_PRESTAMOS = 3

    def __init__(self, nombre, identificacion):
        self.__nombre = self.__validar_nombre(nombre)
        self.__identificacion = self.__validar_identificacion(identificacion)
        self.__prestamos_activos = []      # Lista de nombres de equipos prestados

    # -------------------------------------------------------------------------
    # Métodos privados de validación
    # -------------------------------------------------------------------------

    def __validar_nombre(self, nombre):
        """Valida que el nombre no esté vacío."""
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre del usuario no puede estar vacío.")
        return nombre.strip().title()

    def __validar_identificacion(self, identificacion):
        """Valida que la identificación sea un string no vacío."""
        if not isinstance(identificacion, str) or not identificacion.strip():
            raise ValueError("La identificación no puede estar vacía.")
        return identificacion.strip()

    # -------------------------------------------------------------------------
    # Propiedades
    # -------------------------------------------------------------------------

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        """Permite actualizar el nombre con validación."""
        self.__nombre = self.__validar_nombre(nuevo_nombre)

    @property
    def identificacion(self):
        return self.__identificacion

    @property
    def prestamos_activos(self):
        """Retorna copia de la lista de préstamos activos."""
        return self.__prestamos_activos.copy()

    @property
    def cantidad_prestamos(self):
        """Retorna cuántos préstamos activos tiene el usuario."""
        return len(self.__prestamos_activos)

    @property
    def puede_pedir_prestamo(self):
        """Retorna True si el usuario no ha alcanzado el límite de préstamos."""
        return self.cantidad_prestamos < Usuario.LIMITE_PRESTAMOS

    # -------------------------------------------------------------------------
    # Métodos públicos
    # -------------------------------------------------------------------------

    def agregar_prestamo(self, nombre_equipo):
        """
        Registra un equipo como prestado a este usuario.
        Retorna False si se superó el límite.
        """
        if not self.puede_pedir_prestamo:
            return False
        self.__prestamos_activos.append(nombre_equipo)
        return True

    def quitar_prestamo(self, nombre_equipo):
        """
        Elimina un equipo de la lista de préstamos activos del usuario.
        Retorna False si el equipo no estaba en su lista.
        """
        if nombre_equipo not in self.__prestamos_activos:
            return False
        self.__prestamos_activos.remove(nombre_equipo)
        return True

    def __str__(self):
        return f"{self.__nombre} (ID: {self.__identificacion})"

    def __repr__(self):
        return f"Usuario(nombre='{self.__nombre}', id='{self.__identificacion}')"


# =============================================================================
# CLASE: Prestamo
# Representa la operación de préstamo entre un Usuario y un Equipo.
# Encapsula: equipo, usuario, fecha de préstamo y estado.
# =============================================================================

class Prestamo:
    """
    Modela la transacción de préstamo entre un usuario y un equipo.
    Almacena la información de forma inmutable mediante propiedades.
    """

    def __init__(self, equipo, usuario):
        self.__equipo = equipo
        self.__usuario = usuario
        self.__fecha_prestamo = date.today().strftime("%d/%m/%Y")
        self.__fecha_devolucion = None
        self.__activo = True

    # -------------------------------------------------------------------------
    # Propiedades de solo lectura (no tienen setter)
    # -------------------------------------------------------------------------

    @property
    def equipo(self):
        return self.__equipo

    @property
    def usuario(self):
        return self.__usuario

    @property
    def fecha_prestamo(self):
        return self.__fecha_prestamo

    @property
    def activo(self):
        return self.__activo

    @property
    def fecha_devolucion(self):
        return self.__fecha_devolucion if self.__fecha_devolucion else "Aún no devuelto"

    @property
    def resumen(self):
        """Retorna un texto con el resumen del préstamo."""
        estado = "ACTIVO" if self.__activo else "CERRADO"
        return (
            f"  Equipo:          {self.__equipo.nombre}\n"
            f"  Usuario:         {self.__usuario.nombre} (ID: {self.__usuario.identificacion})\n"
            f"  Fecha préstamo:  {self.__fecha_prestamo}\n"
            f"  Devolución:      {self.fecha_devolucion}\n"
            f"  Estado:          {estado}"
        )

    # -------------------------------------------------------------------------
    # Métodos públicos
    # -------------------------------------------------------------------------

    def cerrar(self):
        """
        Cierra el préstamo registrando la fecha de devolución.
        Retorna False si el préstamo ya estaba cerrado.
        """
        if not self.__activo:
            return False
        self.__fecha_devolucion = date.today().strftime("%d/%m/%Y")
        self.__activo = False
        return True

    def __str__(self):
        return (
            f"Préstamo [{self.__equipo.nombre}] → "
            f"{self.__usuario.nombre} | {self.__fecha_prestamo}"
        )


# =============================================================================
# CLASE: SistemaPrestamos
# Controlador principal del sistema. Gestiona equipos, usuarios y préstamos.
# Encapsula: inventario (dict), usuarios (dict) y registro de préstamos (list).
# =============================================================================

class SistemaPrestamos:
    """
    Gestiona el inventario de equipos, el registro de usuarios
    y todas las operaciones de préstamo y devolución.
    """

    def __init__(self):
        # Diccionario de equipos: clave = nombre del equipo, valor = objeto Equipo
        self.__equipos = {}
        # Diccionario de usuarios: clave = identificación, valor = objeto Usuario
        self.__usuarios = {}
        # Lista de todos los préstamos realizados (objetos Prestamo)
        self.__prestamos = []

        # Cargamos datos iniciales de demostración
        self.__cargar_datos_iniciales()

    # -------------------------------------------------------------------------
    # Métodos privados auxiliares
    # -------------------------------------------------------------------------

    def __cargar_datos_iniciales(self):
        """Carga equipos y usuarios de muestra para demostración."""
        equipos_iniciales = [
            "Laptop Dell Inspiron",
            "Laptop HP Pavilion",
            "Tablet Samsung",
            "Proyector Epson",
            "Cámara Canon"
        ]
        for nombre in equipos_iniciales:
            self.__equipos[nombre] = Equipo(nombre)

        usuarios_iniciales = [
            ("María Pérez",   "CC-1001"),
            ("Carlos Gómez",  "CC-1002"),
            ("Laura Torres",  "CC-1003"),
        ]
        for nombre, identificacion in usuarios_iniciales:
            self.__usuarios[identificacion] = Usuario(nombre, identificacion)

    def __buscar_equipo(self, nombre):
        """Retorna el objeto Equipo si existe, o None."""
        return self.__equipos.get(nombre, None)

    def __buscar_usuario(self, identificacion):
        """Retorna el objeto Usuario si existe, o None."""
        return self.__usuarios.get(identificacion, None)

    def __separador(self, titulo=""):
        """Imprime una línea separadora con título opcional."""
        linea = "=" * 60
        if titulo:
            print(f"\n{linea}")
            print(f"  {titulo}")
            print(linea)
        else:
            print(linea)

    # -------------------------------------------------------------------------
    # Propiedades del sistema
    # -------------------------------------------------------------------------

    @property
    def total_equipos(self):
        return len(self.__equipos)

    @property
    def equipos_disponibles(self):
        return [e for e in self.__equipos.values() if e.disponible]

    @property
    def equipos_prestados(self):
        return [e for e in self.__equipos.values() if not e.disponible]

    @property
    def prestamos_activos(self):
        return [p for p in self.__prestamos if p.activo]

    # -------------------------------------------------------------------------
    # Función 1: Mostrar equipos
    # -------------------------------------------------------------------------

    def mostrar_equipos(self):
        """Muestra todos los equipos y su estado actual."""
        self.__separador("INVENTARIO DE EQUIPOS")

        if not self.__equipos:
            print("  No hay equipos registrados en el sistema.")
            return

        print(f"  {'#':<4} {'EQUIPO':<30} {'ESTADO':<15}")
        print(f"  {'-'*4} {'-'*30} {'-'*15}")

        for i, equipo in enumerate(self.__equipos.values(), start=1):
            estado = equipo.estado
            indicador = "✔" if equipo.disponible else "✘"
            print(f"  {i:<4} {equipo.nombre:<30} {indicador} {estado}")

        print(f"\n  Total: {self.total_equipos} equipo(s) | "
              f"Disponibles: {len(self.equipos_disponibles)} | "
              f"Prestados: {len(self.equipos_prestados)}")

    # -------------------------------------------------------------------------
    # Función 2: Registrar préstamo
    # -------------------------------------------------------------------------

    def registrar_prestamo(self):
        """Registra un nuevo préstamo solicitando equipo y usuario."""
        self.__separador("REGISTRAR PRÉSTAMO")

        # Mostrar solo equipos disponibles
        disponibles = self.equipos_disponibles
        if not disponibles:
            print("  ❌ No hay equipos disponibles en este momento.")
            return

        print("  Equipos disponibles:")
        for i, equipo in enumerate(disponibles, start=1):
            print(f"    {i}. {equipo.nombre}")

        # Solicitar equipo
        nombre_equipo = input("\n  Ingrese el nombre exacto del equipo a prestar: ").strip()
        equipo = self.__buscar_equipo(nombre_equipo)

        if not equipo:
            print(f"  ❌ El equipo '{nombre_equipo}' no existe en el sistema.")
            return
        if not equipo.disponible:
            print(f"  ❌ El equipo '{nombre_equipo}' no está disponible.")
            return

        # Solicitar usuario
        print("\n  Usuarios registrados:")
        for usuario in self.__usuarios.values():
            print(f"    ID: {usuario.identificacion} | {usuario.nombre}")

        id_usuario = input("\n  Ingrese la identificación del usuario: ").strip()
        usuario = self.__buscar_usuario(id_usuario)

        if not usuario:
            print(f"  ❌ No existe un usuario con ID '{id_usuario}'.")
            return
        if not usuario.puede_pedir_prestamo:
            print(f"  ❌ {usuario.nombre} ya tiene {Usuario.LIMITE_PRESTAMOS} préstamos activos.")
            return

        # Crear y registrar el préstamo
        prestamo = Prestamo(equipo, usuario)
        equipo.registrar_prestamo(usuario.nombre)
        usuario.agregar_prestamo(equipo.nombre)
        self.__prestamos.append(prestamo)

        print(f"\n  ✅ Préstamo registrado exitosamente:")
        print(f"     Equipo: {equipo.nombre}")
        print(f"     Usuario: {usuario.nombre}")
        print(f"     Fecha: {prestamo.fecha_prestamo}")

    # -------------------------------------------------------------------------
    # Función 3: Devolver equipo
    # -------------------------------------------------------------------------

    def devolver_equipo(self):
        """Registra la devolución de un equipo prestado."""
        self.__separador("DEVOLVER EQUIPO")

        prestados = self.equipos_prestados
        if not prestados:
            print("  ℹ️  No hay equipos prestados actualmente.")
            return

        print("  Equipos actualmente prestados:")
        for i, equipo in enumerate(prestados, start=1):
            ultimo = equipo.ultimo_prestamo()
            usuario_txt = ultimo[0] if ultimo else "Desconocido"
            print(f"    {i}. {equipo.nombre} → prestado a: {usuario_txt}")

        nombre_equipo = input("\n  Ingrese el nombre exacto del equipo a devolver: ").strip()
        equipo = self.__buscar_equipo(nombre_equipo)

        if not equipo:
            print(f"  ❌ El equipo '{nombre_equipo}' no existe en el sistema.")
            return
        if equipo.disponible:
            print(f"  ❌ El equipo '{nombre_equipo}' no está prestado actualmente.")
            return

        # Cerrar el préstamo activo correspondiente
        for prestamo in reversed(self.__prestamos):
            if prestamo.equipo.nombre == nombre_equipo and prestamo.activo:
                prestamo.cerrar()
                prestamo.usuario.quitar_prestamo(nombre_equipo)
                break

        equipo.registrar_devolucion()

        print(f"\n  ✅ Devolución registrada exitosamente.")
        print(f"     Equipo: {equipo.nombre}")
        print(f"     Fecha de devolución: {date.today().strftime('%d/%m/%Y')}")

    # -------------------------------------------------------------------------
    # Función 4: Ver historial
    # -------------------------------------------------------------------------

    def ver_historial(self):
        """Muestra el historial completo de préstamos por equipo."""
        self.__separador("HISTORIAL DE PRÉSTAMOS")

        hay_historial = False

        for equipo in self.__equipos.values():
            if equipo.tiene_historial():
                hay_historial = True
                print(f"\n  📦 {equipo.nombre} [{equipo.estado}]")
                for i, (usuario, fecha) in enumerate(equipo.historial, start=1):
                    print(f"      {i}. {usuario} — {fecha}")
            else:
                print(f"\n  📦 {equipo.nombre}")
                print(f"      Sin préstamos registrados.")

        if not hay_historial:
            print("\n  No se han realizado préstamos todavía.")

    # -------------------------------------------------------------------------
    # Función 5: Agregar equipo
    # -------------------------------------------------------------------------

    def agregar_equipo(self):
        """Agrega un nuevo equipo al inventario del sistema."""
        self.__separador("AGREGAR NUEVO EQUIPO")

        nombre = input("  Ingrese el nombre del nuevo equipo: ").strip()

        if not nombre:
            print("  ❌ El nombre no puede estar vacío.")
            return

        if nombre in self.__equipos:
            print(f"  ❌ Ya existe un equipo con el nombre '{nombre}'.")
            return

        self.__equipos[nombre] = Equipo(nombre)
        print(f"\n  ✅ Equipo '{nombre}' agregado exitosamente al inventario.")

    # -------------------------------------------------------------------------
    # Función 6: Agregar usuario
    # -------------------------------------------------------------------------

    def agregar_usuario(self):
        """Registra un nuevo usuario en el sistema."""
        self.__separador("AGREGAR NUEVO USUARIO")

        nombre = input("  Ingrese el nombre del usuario: ").strip()
        identificacion = input("  Ingrese la identificación (ej. CC-1234): ").strip()

        if identificacion in self.__usuarios:
            print(f"  ❌ Ya existe un usuario con ID '{identificacion}'.")
            return

        try:
            nuevo_usuario = Usuario(nombre, identificacion)
            self.__usuarios[identificacion] = nuevo_usuario
            print(f"\n  ✅ Usuario '{nuevo_usuario.nombre}' registrado exitosamente.")
        except ValueError as e:
            print(f"  ❌ Error: {e}")

    # -------------------------------------------------------------------------
    # Función 7: Ver préstamos activos
    # -------------------------------------------------------------------------

    def ver_prestamos_activos(self):
        """Muestra todos los préstamos que aún están activos."""
        self.__separador("PRÉSTAMOS ACTIVOS")

        activos = self.prestamos_activos

        if not activos:
            print("  ℹ️  No hay préstamos activos en este momento.")
            return

        for i, prestamo in enumerate(activos, start=1):
            print(f"\n  Préstamo #{i}:")
            print(prestamo.resumen)

    # -------------------------------------------------------------------------
    # Menú principal del sistema
    # -------------------------------------------------------------------------

    def menu(self):
        """Menú interactivo principal del sistema."""
        while True:
            self.__separador("SISTEMA DE PRÉSTAMOS DE EQUIPOS")
            print("  1. Ver inventario de equipos")
            print("  2. Registrar préstamo")
            print("  3. Devolver equipo")
            print("  4. Ver historial de préstamos")
            print("  5. Agregar nuevo equipo")
            print("  6. Agregar nuevo usuario")
            print("  7. Ver préstamos activos")
            print("  8. Salir")
            self.__separador()

            opcion = input("  Seleccione una opción (1-8): ").strip()

            if opcion == "1":
                self.mostrar_equipos()
            elif opcion == "2":
                self.registrar_prestamo()
            elif opcion == "3":
                self.devolver_equipo()
            elif opcion == "4":
                self.ver_historial()
            elif opcion == "5":
                self.agregar_equipo()
            elif opcion == "6":
                self.agregar_usuario()
            elif opcion == "7":
                self.ver_prestamos_activos()
            elif opcion == "8":
                print("\n  👋 Hasta luego. Cerrando el sistema...\n")
                break
            else:
                print("\n  ⚠️  Opción no válida. Por favor ingrese un número entre 1 y 8.")

            input("\n  Presione ENTER para continuar...")


# =============================================================================
# PUNTO DE ENTRADA
# =============================================================================

if __name__ == "__main__":
    sistema = SistemaPrestamos()
    sistema.menu()