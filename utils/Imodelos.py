import abc
from utils.utils import XY


class Modelo(abc.ABCMeta):

    @abc.abstractmethod
    def __init__(self, caracteristicas: int, clases: int, configuracion: dict) -> None:
        pass

    @property
    def modelo(self):
        return self.modelo

    @abc.abstractmethod
    def obtener_parametros_modelo(self):
        pass

    @abc.abstractmethod
    def asignar_parametros_modelo(self, parametros):
        pass

    @abc.abstractmethod
    def entrenar_modelo(self, datos_xy: XY):
        pass

    @abc.abstractmethod
    def evaluar_modelo(self, datos_pruebas: XY):
        pass