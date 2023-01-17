from inspect import getmembers, isclass, isabstract
import vehicles
from creational.factory.simple_factory.vehicles import Vehicle


class VehicleFactory(object):
    vehicles = {}

    def __init__(self):
        self.load_vehicles()

    def load_vehicles(self):
        classes = getmembers(vehicles,
                             lambda v: isclass(v) and not isabstract(v))

        for name, _type in classes:
            if isclass(_type) and issubclass(_type, Vehicle):
                self.vehicles.update([[name, _type]])

    def create_instance(self, name: str) -> Vehicle:
        if name in self.vehicles:
            return self.vehicles[name]()
        else:
            return vehicles.NullVehicle(name)
