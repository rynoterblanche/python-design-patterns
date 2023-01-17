from creational.factory.full_factory.vehicles import Vehicle


class NullVehicle(Vehicle):

    def start(self):
        print(f"NullVehicle '{self._name}' started")

    def stop(self):
        print(f"NullVehicle '{self._name}' stopped")
