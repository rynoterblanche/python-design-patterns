from creational.abstract_factory.vehicles.vehicle import Vehicle


class ChevyCamaro(Vehicle):
    def start(self):
        print("Started ChevyCamaro")

    def stop(self):
        print("Stopped ChevyCamaro")
