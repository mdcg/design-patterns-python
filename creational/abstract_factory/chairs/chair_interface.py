from abc import ABC, abstractmethod


class ChairInterface(ABC):
    @abstractmethod
    def sit_down(self) -> str:
        pass

    @abstractmethod
    def get_up(self) -> str:
        pass
