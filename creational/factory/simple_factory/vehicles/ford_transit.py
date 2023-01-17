from creational.factory.simple_factory.vehicles.vehicle import Vehicle


class FordTransit(Vehicle):
    def start(self):
        print("Ford Transit started")

    def stop(self):
        print("Ford Transit stopped")
