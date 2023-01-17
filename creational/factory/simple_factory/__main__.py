from creational.factory.simple_factory.vehicle_factory import VehicleFactory

factory = VehicleFactory()

for vehicle_name in "FordTransit", "VWPolo", "UnknownVehicle":
    vehicle = factory.create_instance(vehicle_name)
    vehicle.start()
    vehicle.stop()
