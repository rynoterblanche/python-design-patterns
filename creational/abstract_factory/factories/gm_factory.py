from creational.abstract_factory.factories.vehicle_factory import VehicleFactory
from creational.abstract_factory.vehicles.gm.cadillac_cts import CadillacCTS
from creational.abstract_factory.vehicles.gm.chevy_camaro import ChevyCamaro
from creational.abstract_factory.vehicles.gm.chevy_spark import ChevySpark


class GmFactory(VehicleFactory):
    @staticmethod
    def create_economy():
        return ChevySpark()

    @staticmethod
    def create_sport():
        return ChevyCamaro()

    @staticmethod
    def create_luxury():
        return CadillacCTS()
