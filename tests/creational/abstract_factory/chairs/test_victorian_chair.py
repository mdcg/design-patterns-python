import pytest

from creational.abstract_factory.chairs.victorian_chair import VictorianChair


class VictorianChairFixture:
    @pytest.fixture()
    def victorian_chair(self):
        return VictorianChair()
