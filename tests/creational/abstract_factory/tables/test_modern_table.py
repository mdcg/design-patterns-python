import pytest

from creational.abstract_factory.tables.modern_table import ModernTable


class ModernTableFixture:
    @pytest.fixture()
    def modern_table(self):
        return ModernTable()


class TestModernTable(ModernTableFixture):
    def test_prepare_for_dinner(self, modern_table):
        assert modern_table.prepare_for_dinner() == "The super modern user has prepared the table for dinner."

    def test_prepare_for_lunch(self, modern_table):
        assert modern_table.prepare_for_lunch() == "The super modern user has prepared the table for lunch."
