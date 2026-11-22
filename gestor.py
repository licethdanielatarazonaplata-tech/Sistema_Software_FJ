
# gestor.py

import os
import logging

from excepciones import (
    ClienteInvalidoError,
    RegistroDuplicadoError,
    ReservaError
)

from reservas import Reserva


# Crear automáticamente la carpeta de registros.
os.makedirs("logs", exist_ok=True)

# Configurar el sistema de registros.
logging.basicConfig(
    filename="logs/sistema.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)


# Clase encargada de administrar el sistema.
class Gestor:

    def __init__(self):
        # Listas internas, sin utilizar bases de datos.
        self.clientes = []
        self.servicios = []
        self.reservas = []

    # Registrar clientes.
    def registrar_cliente(self, cliente):

        try:
            if cliente is None:
                raise ClienteInvalidoError("El cliente no es válido.")

            for existente in self.clientes:
                if existente.identificacion == cliente.identificacion:
                    raise RegistroDuplicadoError(
                        "El cliente ya se encuentra registrado."
                    )

            self.clientes.append(cliente)

        except (ClienteInvalidoError, RegistroDuplicadoError):
            logging.exception("Error al registrar cliente.")
            raise

        except Exception as error:
            logging.exception("Error inesperado al registrar cliente.")
            raise ClienteInvalidoError(
                "No fue posible registrar el cliente."
            ) from error

        else:
            logging.info(
                "Cliente registrado: %s", cliente.identificacion
            )
            return True

        finally:
            logging.info("Finalizó el intento de registro de cliente.")

    # Registrar servicios.
    def registrar_servicio(self, servicio):

        try:
            if servicio is None:
                raise ValueError("El servicio no puede estar vacío.")

            for existente in self.servicios:
                if existente.identificacion == servicio.identificacion:
                    raise RegistroDuplicadoError(
                        "El servicio ya existe."
                    )

            self.servicios.append(servicio)

        except Exception:
            logging.exception("Error al registrar servicio.")
            raise

        else:
            logging.info("Servicio registrado: %s", servicio.nombre)
            return True

        finally:
            logging.info("Finalizó el intento de registro de servicio.")

    # Buscar un cliente.
    def buscar_cliente(self, identificacion):

        for cliente in self.clientes:
            if cliente.identificacion == identificacion:
                return cliente

        logging.warning("Cliente no encontrado: %s", identificacion)
        return None

    # Buscar un servicio.
    def buscar_servicio(self, identificacion):

        for servicio in self.servicios:
            if servicio.identificacion == identificacion:
                return servicio

        logging.warning("Servicio no encontrado: %s", identificacion)
        return None

    # Crear reservas.
    def crear_reserva(self, identificacion, id_cliente, id_servicio, duracion):

        try:
            cliente = self.buscar_cliente(id_cliente)
            servicio = self.buscar_servicio(id_servicio)

            if cliente is None:
                raise ValueError("El cliente no existe.")

            if servicio is None:
                raise ValueError("El servicio no existe.")

            for existente in self.reservas:
                if existente.identificacion == identificacion:
                    raise RegistroDuplicadoError(
                        "La reserva ya existe."
                    )

            reserva = Reserva(
                identificacion, cliente, servicio, duracion
            )

            self.reservas.append(reserva)

        except RegistroDuplicadoError:
            logging.exception("La reserva está duplicada.")
            raise

        except Exception as error:
            logging.exception("Error al crear reserva.")
            raise ReservaError(
                "No se pudo crear la reserva."
            ) from error

        else:
            logging.info("Reserva creada: %s", identificacion)
            return reserva

        finally:
            logging.info("Finalizó el intento de creación de reserva.")

    # Mostrar todos los clientes.
    def listar_clientes(self):

        for cliente in self.clientes:
            print(cliente.describir())

    # Mostrar todos los servicios.
    def listar_servicios(self):

        for servicio in self.servicios:
            print(servicio.describir())

    # Mostrar todas las reservas.
    def listar_reservas(self):

        for reserva in self.reservas:
            print(reserva.describir())
            print("-" * 40)
