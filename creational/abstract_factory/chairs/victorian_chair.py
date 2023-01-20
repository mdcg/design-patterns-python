from creational.abstract_factory.chairs.chair_interface import ChairInterface


class VictorianChair(ChairInterface):
    def sit_down(self) -> str:
        return "The mega classic user has successfully sat down on the chair."

    def get_up(self) -> str:
        return "The mega classic user got up on the chair successfully."
