from creational.abstract_factory.tables.table_interface import TableInterface


class VictorianTable(TableInterface):
    def prepare_for_dinner(self) -> str:
        return "The mega classic user has prepared the table for dinner."

    def prepare_for_lunch(self) -> str:
        return "The mega classic user has prepared the table for lunch."
