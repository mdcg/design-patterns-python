import pytest

from creational.abstract_factory.sofas.victorian_sofa import VictorianSofa


class VictorianSofaFixture:
    @pytest.fixture()
    def victorian_sofa(self):
        return VictorianSofa()


class TestVictorianSofa(VictorianSofaFixture):
    def test_relax(self, victorian_sofa):
        assert victorian_sofa.relax() == "The mega classic user relaxed on sofa."
