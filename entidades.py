
# entidades.py

from abc import ABC, abstractmethod


# Clase abstracta que representa una entidad general.
class Entidad(ABC):

    def __init__(self, identificacion):
        self.__identificacion = identificacion

    # Método para consultar la identificación.
    @property
    def identificacion(self):
        return self.__identificacion

    # Método abstracto que deben implementar las clases hijas.
    @abstractmethod
    def describir(self):
        pass
