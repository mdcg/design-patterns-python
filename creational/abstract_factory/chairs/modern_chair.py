from creational.abstract_factory.chairs.chair_interface import ChairInterface


class ModernChair(ChairInterface):
    def sit_down(self) -> str:
        return "The super modern user has successfully sat down on the chair."

    def get_up(self) -> str:
        return "The super modern user got up on the chair successfully."
