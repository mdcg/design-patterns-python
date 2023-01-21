import pytest

from creational.abstract_factory.funitures.victorian_funiture_factory import VictorianFunitureFactory


class VictorianFunitureFactoryFixture:
    @pytest.fixture()
    def victorian_funiture_factory(self):
        return VictorianFunitureFactory()
