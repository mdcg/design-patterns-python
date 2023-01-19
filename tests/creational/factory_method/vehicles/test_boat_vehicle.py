from creational.factory_method.vehicles.boat import Boat


class TestBoat:
    def test_should_return_a_message_corresponding_to_the_beginning_of_the_expedition_by_boat(self):
        assert Boat().deliver() == "Expedition started successfully (Boat)."
