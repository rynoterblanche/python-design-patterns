from creational.factory.simple_factory.vehicles.vehicle import Vehicle


class NullVehicle(Vehicle):

    def __init__(self, name: str):
        self._name = name

    def start(self):
        print(f"NullVehicle '{self._name}' started")

    def stop(self):
        print(f"NullVehicle '{self._name}' stopped")
