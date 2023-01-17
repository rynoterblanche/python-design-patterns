from creational.factory.full_factory.factories.vehicle_factory import VehicleFactory
from creational.factory.full_factory.vehicles import Vehicle, Tesla


class TeslaFactory(VehicleFactory):
    def create_vehicle(self) -> Vehicle:
        vehicle = Tesla()
        vehicle.name = "Tesla"
        return vehicle
