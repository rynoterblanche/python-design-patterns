from creational.factory.full_factory.factories import loader

for factory_name in "porsche_factory", "tesla_factory", "unknown_vehicle_factory":
    factory = loader.load_factory(factory_name)

    vehicle = factory.create_vehicle()
    vehicle.start()
    vehicle.stop()


for vehicle_name in "porsche", "tesla", "unknown_vehicle":
    factory = loader.load_factory_by_vehicle_name(vehicle_name)

    vehicle = factory.create_vehicle()
    vehicle.start()
    vehicle.stop()