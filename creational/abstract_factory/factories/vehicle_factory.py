from abc import ABC, abstractmethod


class VehicleFactory(ABC):

    @staticmethod
    @abstractmethod
    def create_economy():
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def create_sport():
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def create_luxury():
        raise NotImplementedError
