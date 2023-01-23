import pytest

from creational.abstract_factory.chairs.modern_chair import ModernChair
from creational.abstract_factory.funitures.modern_funiture_factory import ModernFunitureFactory
from creational.abstract_factory.sofas.modern_sofa import ModernSofa
from creational.abstract_factory.tables.modern_table import ModernTable


class ModernFunitureFactoryFixture:
    @pytest.fixture()
    def modern_funiture_factory(self):
        return ModernFunitureFactory()


class TestModernFunitureFactory(ModernFunitureFactoryFixture):
    def test_create_chair(self, modern_funiture_factory):
        assert isinstance(modern_funiture_factory.create_chair(), ModernChair)

    def test_create_sofa(self, modern_funiture_factory):
        assert isinstance(modern_funiture_factory.create_sofa(), ModernSofa)

    def test_create_table(self, modern_funiture_factory):
        assert isinstance(modern_funiture_factory.create_table(), ModernTable)
