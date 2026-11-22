
# clientes.py

from entidades import Entidad
from excepciones import ClienteInvalidoError


class Cliente(Entidad):

    def __init__(self, identificacion, nombre, correo, telefono):

        # Inicializar la clase padre.
        super().__init__(identificacion)

        # Validar los datos del cliente.
        if not isinstance(nombre, str) or not nombre.strip():
            raise ClienteInvalidoError("El nombre no puede estar vacío.")

        if not isinstance(correo, str) or "@" not in correo or "." not in correo:
            raise ClienteInvalidoError("El correo electrónico no es válido.")

        if not isinstance(telefono, str) or not telefono.isdigit() or len(telefono) < 7:
            raise ClienteInvalidoError("El teléfono debe tener mínimo 7 dígitos.")

        # Datos privados del cliente.
        self.__nombre = nombre.strip()
        self.__correo = correo.strip()
        self.__telefono = telefono.strip()

    # Consultar nombre.
    @property
    def nombre(self):
        return self.__nombre

    # Consultar correo.
    @property
    def correo(self):
        return self.__correo

    # Consultar teléfono.
    @property
    def telefono(self):
        return self.__telefono

    # Describir la información del cliente.
    def describir(self):
        return (
            f"Cliente: {self.__nombre} | "
            f"Correo: {self.__correo} | "
            f"Teléfono: {self.__telefono}"
        )
