from creational.factory_method.logistics.sea_logistic import SeaLogistic
from creational.factory_method.vehicles.boat import Boat


class TestSeaLogistic:
    def test_sea_logistic_should_return_a_boat_instance_when_create_transport_method_called(self):
        logistic = SeaLogistic()
        assert isinstance(logistic.create_transport(), Boat)
