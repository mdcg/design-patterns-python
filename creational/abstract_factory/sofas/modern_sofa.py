from creational.abstract_factory.sofas.sofa_interface import SofaInterface


class ModernSofa(SofaInterface):
    def relax(self) -> str:
        return "The super modern user relaxed on sofa."
