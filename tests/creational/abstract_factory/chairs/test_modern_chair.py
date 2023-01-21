import pytest

from creational.abstract_factory.chairs.modern_chair import ModernChair


class ModernChairFixture:
    @pytest.fixture()
    def modern_chair(self):
        return ModernChair()
