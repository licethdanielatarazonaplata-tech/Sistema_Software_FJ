
# reservas.py

from entidades import Entidad
from clientes import Cliente
from servicios import Servicio
from excepciones import ReservaError, DatosInvalidosError


class Reserva(Entidad):

    def __init__(self, identificacion, cliente, servicio, duracion):

        super().__init__(identificacion)

        # Validar que se haya seleccionado un cliente.
        if not isinstance(cliente, Cliente):
            raise DatosInvalidosError(
                "Debe seleccionar un cliente válido."
            )

        # Validar que se haya seleccionado un servicio.
        if not isinstance(servicio, Servicio):
            raise DatosInvalidosError(
                "Debe seleccionar un servicio válido."
            )

        # Validar la duración.
        if not isinstance(duracion, (int, float)) or isinstance(duracion, bool) or duracion <= 0:
            raise DatosInvalidosError(
                "La duración debe ser mayor que cero."
            )

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"
        self.costo = 0

    # Confirmar una reserva.
    def confirmar(self):

        if self.estado != "Pendiente":
            raise ReservaError(
                "La reserva no se puede confirmar."
            )

        self.servicio.validar_parametros(self.duracion)
        self.estado = "Confirmada"

        return "Reserva confirmada correctamente."

    # Cancelar una reserva.
    def cancelar(self):

        if self.estado == "Cancelada":
            raise ReservaError(
                "La reserva ya está cancelada."
            )

        if self.estado == "Procesada":
            raise ReservaError(
                "No se puede cancelar una reserva procesada."
            )

        self.estado = "Cancelada"

        return "Reserva cancelada correctamente."

    # Procesar una reserva.
    def procesar(self, impuesto=0, descuento=0):

        if self.estado != "Confirmada":
            raise ReservaError(
                "Solo se pueden procesar reservas confirmadas."
            )

        try:
            self.costo = self.servicio.calcular_costo(
                self.duracion,
                impuesto,
                descuento
            )

            self.estado = "Procesada"

            return self.costo

        except DatosInvalidosError as error:
            raise ReservaError(
                "No fue posible procesar el costo de la reserva."
            ) from error

    # Mostrar la información de la reserva.
    def describir(self):

        return (
            f"Reserva: {self.identificacion}\n"
            f"Cliente: {self.cliente.nombre}\n"
            f"Servicio: {self.servicio.nombre}\n"
            f"Duración: {self.duracion} horas\n"
            f"Estado: {self.estado}\n"
            f"Costo: ${self.costo:,.2f}"
        )
