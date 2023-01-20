from creational.factory_method.logistics.logistic import Logistic
from creational.factory_method.vehicles.boat import Boat
from creational.factory_method.vehicles.vehicle import Vehicle


class SeaLogistic(Logistic):
    def create_transport(self) -> Vehicle:
        return Boat()
