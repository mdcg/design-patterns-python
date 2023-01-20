from creational.abstract_factory.chairs.modern_chair import ModernChair
from creational.abstract_factory.funitures.funiture_factory_interface import FunitureInterface
from creational.abstract_factory.sofas.modern_sofa import ModernSofa
from creational.abstract_factory.tables.modern_table import ModernTable


class ModernFunitureFactory(FunitureInterface):
    def create_chair(self) -> ModernChair:
        return ModernTable()

    def create_sofa(self) -> ModernSofa:
        return ModernSofa()

    def create_table(self) -> ModernTable:
        return ModernSofa()
