
# excepciones.py

# Excepción para errores relacionados con clientes.
class ClienteInvalidoError(Exception):
    pass


# Excepción para errores relacionados con servicios.
class ServicioNoDisponibleError(Exception):
    pass


# Excepción para errores relacionados con reservas.
class ReservaError(Exception):
    pass


# Excepción para datos incorrectos.
class DatosInvalidosError(Exception):
    pass


# Excepción para registros que ya existen.
class RegistroDuplicadoError(Exception):
    pass
