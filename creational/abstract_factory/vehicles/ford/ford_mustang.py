from creational.abstract_factory.vehicles.vehicle import Vehicle


class FordMustang(Vehicle):
    def start(self):
        print("Started FordMustang")

    def stop(self):
        print("Stopped FordMustang")
