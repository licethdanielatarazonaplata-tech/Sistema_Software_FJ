
# servicios.py

from abc import abstractmethod
from entidades import Entidad
from excepciones import DatosInvalidosError, ServicioNoDisponibleError


# Clase abstracta Servicio.
class Servicio(Entidad):

    def __init__(self, identificacion, nombre, tarifa_base):
        super().__init__(identificacion)

        if not isinstance(nombre, str) or not nombre.strip():
            raise DatosInvalidosError("El nombre del servicio es obligatorio.")

        if not isinstance(tarifa_base, (int, float)) or isinstance(tarifa_base, bool) or tarifa_base <= 0:
            raise DatosInvalidosError("La tarifa debe ser mayor que cero.")

        self.nombre = nombre.strip()
        self.tarifa_base = float(tarifa_base)
        self.disponible = True

    # Validar disponibilidad del servicio.
    def validar_disponibilidad(self):
        if not self.disponible:
            raise ServicioNoDisponibleError(
                f"El servicio {self.nombre} no está disponible."
            )

    # Método general para validar parámetros.
    def validar_parametros(self, duracion):
        if not isinstance(duracion, (int, float)) or isinstance(duracion, bool) or duracion <= 0:
            raise DatosInvalidosError("La duración debe ser mayor que cero.")

        self.validar_disponibilidad()

    # Cálculo de costos con parámetros opcionales.
    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        self.validar_parametros(duracion)

        if not isinstance(impuesto, (int, float)) or isinstance(impuesto, bool) or not 0 <= impuesto <= 100:
            raise DatosInvalidosError("El impuesto debe estar entre 0 y 100.")

        if not isinstance(descuento, (int, float)) or isinstance(descuento, bool) or not 0 <= descuento <= 100:
            raise DatosInvalidosError("El descuento debe estar entre 0 y 100.")

        costo = self.calcular_base(duracion)
        costo -= costo * (descuento / 100)
        costo += costo * (impuesto / 100)

        return round(costo, 2)

    @abstractmethod
    def calcular_base(self, duracion):
        pass

    @abstractmethod
    def describir(self):
        pass


# Servicio especializado: reserva de salas.
class ReservaSala(Servicio):

    # Validación sobrescrita para reservas de salas.
    def validar_parametros(self, duracion):
        super().validar_parametros(duracion)

        if duracion > 12:
            raise DatosInvalidosError(
                "La reserva de una sala no puede superar 12 horas."
            )

    def calcular_base(self, duracion):
        self.validar_parametros(duracion)
        return self.tarifa_base * duracion

    def describir(self):
        return f"Sala: {self.nombre} - Tarifa por hora: ${self.tarifa_base:,.2f}"


# Servicio especializado: alquiler de equipos.
class AlquilerEquipo(Servicio):

    # Validación sobrescrita para alquiler de equipos.
    def validar_parametros(self, duracion):
        super().validar_parametros(duracion)

        if duracion > 24:
            raise DatosInvalidosError(
                "El alquiler de equipos no puede superar 24 horas."
            )

    def calcular_base(self, duracion):
        self.validar_parametros(duracion)
        return self.tarifa_base * duracion

    def describir(self):
        return f"Equipo: {self.nombre} - Tarifa por hora: ${self.tarifa_base:,.2f}"


# Servicio especializado: asesorías especializadas.
class Asesoria(Servicio):

    # Validación sobrescrita para asesorías.
    def validar_parametros(self, duracion):
        super().validar_parametros(duracion)

        if duracion > 8:
            raise DatosInvalidosError(
                "Una asesoría no puede superar 8 horas."
            )

    def calcular_base(self, duracion):
        self.validar_parametros(duracion)
        return self.tarifa_base * duracion

    def describir(self):
        return f"Asesoría: {self.nombre} - Tarifa por hora: ${self.tarifa_base:,.2f}"

