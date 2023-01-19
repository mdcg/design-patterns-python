import pytest

from creational.factory_method.main import process


class TestMain:
    def test_process_should_return_that_the_expedition_was_started_by_plane_if_the_type_of_logistics_is_air(
        self,
    ):
        assert process("air") == "Expedition started successfully (Plane)."

    def test_process_should_return_that_the_expedition_was_started_by_boat_if_the_type_of_logistics_is_sea(
        self,
    ):
        assert process("sea") == "Expedition started successfully (Boat)."

    def test_should_raise_not_implemented_if_logistic_type_does_not_exists(
        self,
    ):
        with pytest.raises(NotImplementedError):
            process("space")
