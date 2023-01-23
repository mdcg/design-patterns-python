import pytest

from creational.abstract_factory.chairs.victorian_chair import VictorianChair


class VictorianChairFixture:
    @pytest.fixture()
    def victorian_chair(self):
        return VictorianChair()


class TestVictorianChair(VictorianChairFixture):
    def test_sit_down(self, victorian_chair):
        assert victorian_chair.sit_down() == "The mega classic user has successfully sat down on the chair."

    def test_get_up(self, victorian_chair):
        assert victorian_chair.get_up() == "The mega classic user got up on the chair successfully."
