import pytest

from creational.abstract_factory.sofas.modern_sofa import ModernSofa


class ModernSofaFixture:
    @pytest.fixture()
    def modern_sofa(self):
        return ModernSofa()
