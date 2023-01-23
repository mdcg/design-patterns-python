import pytest

from creational.abstract_factory.sofas.modern_sofa import ModernSofa


class ModernSofaFixture:
    @pytest.fixture()
    def modern_sofa(self):
        return ModernSofa()


class TestModernSofa(ModernSofaFixture):
    def test_relax(self, modern_sofa):
        assert modern_sofa.relax() == "The super modern user relaxed on sofa."
