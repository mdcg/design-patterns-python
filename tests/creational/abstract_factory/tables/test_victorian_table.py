import pytest

from creational.abstract_factory.tables.victorian_table import VictorianTable


class VictorianTableFixture:
    @pytest.fixture()
    def victorian_table(self):
        return VictorianTable()


class TestVictorianTable(VictorianTableFixture):
    def test_prepare_for_dinner(self, victorian_table):
        assert victorian_table.prepare_for_dinner() == "The mega classic user has prepared the table for dinner."

    def test_prepare_for_lunch(self, victorian_table):
        assert victorian_table.prepare_for_lunch() == "The mega classic user has prepared the table for lunch."
