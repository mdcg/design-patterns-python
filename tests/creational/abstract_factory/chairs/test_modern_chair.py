import pytest

from creational.abstract_factory.chairs.modern_chair import ModernChair


class ModernChairFixture:
    @pytest.fixture()
    def modern_chair(self):
        return ModernChair()


class TestModernChair(ModernChairFixture):
    def test_sit_down(self, modern_chair):
        assert modern_chair.sit_down() == "The super modern user has successfully sat down on the chair."

    def test_get_up(self, modern_chair):
        assert modern_chair.get_up() == "The super modern user got up on the chair successfully."
