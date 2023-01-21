import pytest

from creational.abstract_factory.funitures.modern_funiture_factory import ModernFunitureFactory


class ModernFunitureFactoryFixture:
    @pytest.fixture()
    def modern_funiture_factory(self):
        return ModernFunitureFactory()
