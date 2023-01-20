from abc import ABC, abstractmethod

from creational.abstract_factory.chairs.chair_interface import ChairInterface
from creational.abstract_factory.sofas.sofa_interface import SofaInterface
from creational.abstract_factory.tables.table_interface import TableInterface


class FunitureInterface(ABC):
    @abstractmethod
    def create_chair(self) -> ChairInterface:
        pass

    @abstractmethod
    def create_table(self) -> TableInterface:
        pass

    @abstractmethod
    def create_sofa(self) -> SofaInterface:
        pass
