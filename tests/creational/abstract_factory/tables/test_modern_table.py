import pytest

from creational.abstract_factory.tables.modern_table import ModernTable


class ModernTableFixture:
    @pytest.fixture()
    def modern_table(self):
        return ModernTable()
