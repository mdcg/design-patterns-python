import pytest

from creational.abstract_factory.sofas.victorian_sofa import VictorianSofa


class VictorianSofaFixture:
    @pytest.fixture()
    def victorian_sofa(self):
        return VictorianSofa()
