from creational.abstract_factory.vehicles.vehicle import Vehicle


class ChevySpark(Vehicle):
    def start(self):
        print("Started ChevySpark")

    def stop(self):
        print("Stopped ChevySpark")
