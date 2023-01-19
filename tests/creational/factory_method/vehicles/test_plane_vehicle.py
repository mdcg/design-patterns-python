from creational.factory_method.vehicles.plane import Plane


class TestPlane:
    def test_should_return_a_message_corresponding_to_the_beginning_of_the_expedition_by_plane(self):
        assert Plane().deliver() == "Expedition started successfully (Plane)."
