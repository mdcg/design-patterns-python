from creational.factory_method.logistics.air_logistic import AirLogistic
from creational.factory_method.vehicles.plane import Plane


class TestAirLogistic:
    def test_air_logistic_should_return_a_plane_instance_when_create_transport_method_called(self):
        logistic = AirLogistic()
        assert isinstance(logistic.create_transport(), Plane)
