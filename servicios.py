
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

    # Validar que el servicio esté disponible.
    def validar_disponibilidad(self):
        if not self.disponible:
            raise ServicioNoDisponibleError(
                f"El servicio {self.nombre} no está disponible."
            )

    # Validar la duración.
    def validar_parametros(self, duracion):
        if not isinstance(duracion, (int, float)) or isinstance(duracion, bool) or duracion <= 0:
            raise DatosInvalidosError("La duración debe ser mayor que cero.")

        self.validar_disponibilidad()

    # Método con parámetros opcionales.
    # Permite calcular costos con impuestos y descuentos.
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

    def calcular_base(self, duracion):
        self.validar_parametros(duracion)
        return self.tarifa_base * duracion

    def describir(self):
        return f"Sala: {self.nombre} - Tarifa por hora: ${self.tarifa_base:,.2f}"


# Servicio especializado: alquiler de equipos.
class AlquilerEquipo(Servicio):

    def calcular_base(self, duracion):
        self.validar_parametros(duracion)
        return self.tarifa_base * duracion

    def describir(self):
        return f"Equipo: {self.nombre} - Tarifa por hora: ${self.tarifa_base:,.2f}"


# Servicio especializado: asesorías especializadas.
class Asesoria(Servicio):

    def calcular_base(self, duracion):
        self.validar_parametros(duracion)
        return self.tarifa_base * duracion

    def describir(self):
        return f"Asesoría: {self.nombre} - Tarifa por hora: ${self.tarifa_base:,.2f}"
