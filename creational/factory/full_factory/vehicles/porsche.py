from creational.factory.full_factory.vehicles import Vehicle


class Porsche(Vehicle):

    def start(self):
        print(f"{self.name} started")

    def stop(self):
        print(f"{self.name} stopped")
