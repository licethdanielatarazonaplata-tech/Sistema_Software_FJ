
# main.py

import logging

from clientes import Cliente
from servicios import ReservaSala, AlquilerEquipo, Asesoria
from gestor import Gestor


# Crear el administrador general del sistema.
sistema = Gestor()


# Función para ejecutar operaciones sin detener el programa.
def ejecutar_operacion(nombre, funcion):

    print("\n" + "=" * 55)
    print("OPERACIÓN:", nombre)
    print("=" * 55)

    try:
        resultado = funcion()

    except Exception as error:
        print("ERROR CONTROLADO:", error)
        logging.exception("Operación fallida: %s", nombre)

    else:
        if resultado is not None:
            print("RESULTADO:", resultado)

        print("Operación ejecutada correctamente.")

    finally:
        print("Finalizó la operación:", nombre)


# -------------------------------------------------
# 1. Registrar un cliente válido.
# -------------------------------------------------

cliente1 = Cliente(
    "C001",
    "Carlos Pérez",
    "carlos@gmail.com",
    "3001234567"
)

ejecutar_operacion(
    "Registrar cliente Carlos",
    lambda: sistema.registrar_cliente(cliente1)
)


# -------------------------------------------------
# 2. Registrar otro cliente válido.
# -------------------------------------------------

cliente2 = Cliente(
    "C002",
    "María Rodríguez",
    "maria@gmail.com",
    "3101234567"
)

ejecutar_operacion(
    "Registrar cliente María",
    lambda: sistema.registrar_cliente(cliente2)
)


# -------------------------------------------------
# 3. Intentar crear un cliente con datos incorrectos.
# -------------------------------------------------

def cliente_invalido():
    Cliente("C003", "", "correo_incorrecto", "123")


ejecutar_operacion(
    "Registrar cliente con datos inválidos",
    cliente_invalido
)


# -------------------------------------------------
# 4. Intentar registrar un cliente duplicado.
# -------------------------------------------------

ejecutar_operacion(
    "Registrar cliente duplicado",
    lambda: sistema.registrar_cliente(cliente1)
)


# -------------------------------------------------
# 5. Registrar servicio de reserva de sala.
# -------------------------------------------------

sala = ReservaSala(
    "S001",
    "Sala de reuniones",
    30000
)

ejecutar_operacion(
    "Registrar servicio de sala",
    lambda: sistema.registrar_servicio(sala)
)


# -------------------------------------------------
# 6. Registrar servicio de alquiler de equipos.
# -------------------------------------------------

equipo = AlquilerEquipo(
    "S002",
    "Computador portátil",
    15000
)

ejecutar_operacion(
    "Registrar servicio de equipos",
    lambda: sistema.registrar_servicio(equipo)
)


# -------------------------------------------------
# 7. Registrar servicio de asesorías.
# -------------------------------------------------

asesoria = Asesoria(
    "S003",
    "Asesoría en programación",
    50000
)

ejecutar_operacion(
    "Registrar servicio de asesoría",
    lambda: sistema.registrar_servicio(asesoria)
)


# -------------------------------------------------
# 8. Intentar crear un servicio con tarifa incorrecta.
# -------------------------------------------------

def servicio_invalido():
    ReservaSala("S004", "Sala incorrecta", -100)


ejecutar_operacion(
    "Crear servicio con tarifa inválida",
    servicio_invalido
)


# -------------------------------------------------
# 9. Crear una reserva válida.
# -------------------------------------------------

reserva1 = None


def crear_reserva1():
    global reserva1

    reserva1 = sistema.crear_reserva(
        "R001", "C001", "S001", 2
    )

    return "Reserva R001 creada."


ejecutar_operacion(
    "Crear reserva válida",
    crear_reserva1
)


# -------------------------------------------------
# 10. Confirmar la reserva.
# -------------------------------------------------

ejecutar_operacion(
    "Confirmar reserva R001",
    lambda: reserva1.confirmar()
)


# -------------------------------------------------
# 11. Procesar la reserva y calcular el costo.
# -------------------------------------------------

ejecutar_operacion(
    "Procesar reserva con impuesto del 19%",
    lambda: reserva1.procesar(19, 0)
)


# -------------------------------------------------
# 12. Intentar crear una reserva con cliente inexistente.
# -------------------------------------------------

ejecutar_operacion(
    "Crear reserva con cliente inexistente",
    lambda: sistema.crear_reserva(
        "R002", "C999", "S001", 2
    )
)


# -------------------------------------------------
# 13. Crear y cancelar una reserva pendiente.
# -------------------------------------------------

reserva2 = None


def crear_reserva2():
    global reserva2

    reserva2 = sistema.crear_reserva(
        "R003", "C002", "S002", 3
    )

    return "Reserva R003 creada."


ejecutar_operacion(
    "Crear segunda reserva",
    crear_reserva2
)

ejecutar_operacion(
    "Cancelar reserva pendiente",
    lambda: reserva2.cancelar()
)


# -------------------------------------------------
# 14. Intentar confirmar un servicio no disponible.
# -------------------------------------------------

reserva3 = None


def probar_servicio_no_disponible():

    global reserva3

    reserva3 = sistema.crear_reserva(
        "R004", "C001", "S003", 1
    )

    asesoria.disponible = False

    try:
        reserva3.confirmar()

    finally:
        # Restablecer la disponibilidad del servicio.
        asesoria.disponible = True


ejecutar_operacion(
    "Intentar reservar servicio no disponible",
    probar_servicio_no_disponible
)


# -------------------------------------------------
# 15. Mostrar todos los registros del sistema.
# -------------------------------------------------

ejecutar_operacion(
    "Mostrar clientes registrados",
    sistema.listar_clientes
)

ejecutar_operacion(
    "Mostrar servicios registrados",
    sistema.listar_servicios
)

ejecutar_operacion(
    "Mostrar reservas registradas",
    sistema.listar_reservas
)


# -------------------------------------------------
# 16. Demostrar diferentes variantes del cálculo.
# -------------------------------------------------

def demostrar_calculos():

    print("Costo normal:", sala.calcular_costo(2))

    print(
        "Costo con impuesto:",
        sala.calcular_costo(2, 19)
    )

    print(
        "Costo con impuesto y descuento:",
        sala.calcular_costo(2, 19, 10)
    )


ejecutar_operacion(
    "Demostrar variantes del cálculo de costos",
    demostrar_calculos
)


print("\n" + "=" * 55)
print("SISTEMA SOFTWARE FJ FINALIZADO")
print("El programa completó sus operaciones de demostración.")
print("Los eventos y errores se guardaron en logs/sistema.log")
print("=" * 55)
