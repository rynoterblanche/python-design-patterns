from creational.factory.full_factory.factories.vehicle_factory import VehicleFactory
from creational.factory.full_factory.vehicles import Vehicle, Porsche


class PorscheFactory(VehicleFactory):
    def create_vehicle(self) -> Vehicle:
        vehicle = Porsche()
        vehicle.name = "Porsche"
        return vehicle

