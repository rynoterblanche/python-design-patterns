from creational.factory.full_factory.factories.vehicle_factory import VehicleFactory
from creational.factory.full_factory.vehicles import Vehicle, NullVehicle


class NullFactory(VehicleFactory):
    def create_vehicle(self) -> Vehicle:
        vehicle = NullVehicle()
        vehicle.name = "NullVehicle"
        return vehicle
