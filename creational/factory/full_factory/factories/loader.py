from importlib import import_module
from inspect import getmembers, isclass, isabstract

from creational.factory.full_factory.factories.vehicle_factory import VehicleFactory


def load_factory(name: str) -> VehicleFactory:
    try:
        factory_module = import_module(f".{name}", "factories")
    except ImportError:
        factory_module = import_module(f".null_factory", "factories")

    classes = getmembers(factory_module,
                         lambda m: isclass(m) and not isabstract(m))

    for _, _class in classes:
        if issubclass(_class, VehicleFactory):
            return _class()


def load_factory_by_vehicle_name(vehicle_name: str) -> VehicleFactory:
    if vehicle_name is None:
        return load_factory("null_factory")

    factory_name = f"{vehicle_name.lower()}_factory"
    return load_factory(factory_name)
