import pytest

from creational.abstract_factory.chairs.victorian_chair import VictorianChair
from creational.abstract_factory.funitures.victorian_funiture_factory import VictorianFunitureFactory
from creational.abstract_factory.sofas.victorian_sofa import VictorianSofa
from creational.abstract_factory.tables.victorian_table import VictorianTable


class VictorianFunitureFactoryFixture:
    @pytest.fixture()
    def victorian_funiture_factory(self):
        return VictorianFunitureFactory()


class TestVictorianFunitureFactory(VictorianFunitureFactoryFixture):
    def test_create_chair(self, victorian_funiture_factory):
        assert isinstance(victorian_funiture_factory.create_chair(), VictorianChair)

    def test_create_sofa(self, victorian_funiture_factory):
        assert isinstance(victorian_funiture_factory.create_sofa(), VictorianSofa)

    def test_create_table(self, victorian_funiture_factory):
        assert isinstance(victorian_funiture_factory.create_table(), VictorianTable)
