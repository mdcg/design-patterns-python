from creational.abstract_factory.sofas.sofa_interface import SofaInterface


class VictorianSofa(SofaInterface):
    def relax(self) -> str:
        return "The mega classic user relaxed on sofa."
