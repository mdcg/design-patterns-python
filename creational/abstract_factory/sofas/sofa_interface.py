from abc import ABC, abstractmethod


class SofaInterface(ABC):
    @abstractmethod
    def relax(self) -> str:
        pass
