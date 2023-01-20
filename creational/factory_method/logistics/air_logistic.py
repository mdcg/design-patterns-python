from creational.factory_method.logistics.logistic import Logistic
from creational.factory_method.vehicles.plane import Plane
from creational.factory_method.vehicles.vehicle import Vehicle


class AirLogistic(Logistic):
    def create_transport(self) -> Vehicle:
        return Plane()
