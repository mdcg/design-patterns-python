import pytest

from creational.abstract_factory.tables.victorian_table import VictorianTable


class ModernTableFixture:
    @pytest.fixture()
    def victorian_table(self):
        return VictorianTable()
