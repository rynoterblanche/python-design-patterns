from abc import ABC, abstractmethod

from creational.factory.full_factory.vehicles import Vehicle


class VehicleFactory(ABC):

    @abstractmethod
    def create_vehicle(self) -> Vehicle:
        raise NotImplementedError
