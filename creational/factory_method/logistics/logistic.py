from abc import ABC, abstractmethod

from creational.factory_method.vehicles.vehicle import Vehicle


class Logistic(ABC):
    @abstractmethod
    def create_transport(self) -> Vehicle:  # noqa
        pass

    def start_expedition(self):
        transport = self.create_transport()
        return transport.deliver()
