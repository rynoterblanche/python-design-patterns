from creational.abstract_factory.factories.vehicle_factory import VehicleFactory
from creational.abstract_factory.vehicles.ford.ford_fiesta import FordFiesta
from creational.abstract_factory.vehicles.ford.ford_mustang import FordMustang
from creational.abstract_factory.vehicles.ford.lincoln_mks import LincolnMKS


class FordFactory(VehicleFactory):
    @staticmethod
    def create_economy():
        return FordFiesta()

    @staticmethod
    def create_sport():
        return FordMustang()

    @staticmethod
    def create_luxury():
        return LincolnMKS()
