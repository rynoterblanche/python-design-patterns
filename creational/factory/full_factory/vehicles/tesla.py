from creational.factory.full_factory.vehicles import Vehicle


class Tesla(Vehicle):

    def start(self):
        print(f"{self.name} started")

    def stop(self):
        print(f"{self.name} stopped")
