from creational.abstract_factory.chairs.victorian_chair import VictorianChair
from creational.abstract_factory.funitures.funiture_factory_interface import FunitureInterface
from creational.abstract_factory.sofas.victorian_sofa import VictorianSofa
from creational.abstract_factory.tables.victorian_table import VictorianTable


class VictorianFunitureFactory(FunitureInterface):
    def create_chair(self) -> VictorianChair:
        return VictorianChair()

    def create_sofa(self) -> VictorianSofa:
        return VictorianSofa()

    def create_table(self) -> VictorianTable:
        return VictorianTable()
