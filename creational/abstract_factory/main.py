from creational.abstract_factory.funitures.modern_funiture_factory import ModernFunitureFactory
from creational.abstract_factory.funitures.victorian_funiture_factory import VictorianFunitureFactory


class Client:
    def __init__(self, funiture_type):
        self.funiture = {
            "modern": ModernFunitureFactory,
            "victorian": VictorianFunitureFactory,
        }.get(funiture_type, NotImplementedError)()

        self.chair = self.funiture.create_chair()
        self.table = self.funiture.create_table()
        self.sofa = self.funiture.create_sofa()

    def enjoy_sofa(self):
        return self.sofa.relax()

    def prepare_table_to_dinner(self):
        return self.table.prepare_for_dinner()

    def prepare_table_to_lunch(self):
        return self.table.prepare_for_lunch()

    def sit_on_the_chair(self):
        return self.chair.sit_down()

    def get_up_from_the_chair(self):
        return self.chair.sit_down()


if __name__ == "__main__":
    client = Client(funiture_type="victorian")
    client.enjoy_sofa()
    client.prepare_table_to_dinner()
    client.prepare_table_to_lunch()
    client.sit_on_the_chair()
    client.get_up_from_the_chair()
