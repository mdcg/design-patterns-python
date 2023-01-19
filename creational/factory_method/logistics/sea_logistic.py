from creational.factory_method.logistics.logistic import Logistic
from creational.factory_method.vehicles.vehicle import Vehicle
from creational.factory_method.vehicles.boat import Boat


class SeaLogistic(Logistic):
    def create_transport(self) -> Vehicle:
        return Boat()
