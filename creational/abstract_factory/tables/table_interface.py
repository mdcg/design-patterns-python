from abc import ABC, abstractmethod


class TableInterface(ABC):
    @abstractmethod
    def prepare_for_dinner(self) -> str:
        pass

    @abstractmethod
    def prepare_for_lunch(self) -> str:
        pass
