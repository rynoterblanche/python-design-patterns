from creational.abstract_factory.factories.ford_factory import FordFactory
from creational.abstract_factory.factories.gm_factory import GmFactory

for factory in FordFactory, GmFactory:
    car = factory.create_economy()
    car.start()
    car.stop()

    car = factory.create_sport()
    car.start()
    car.stop()

    car = factory.create_luxury()
    car.start()
    car.stop()
