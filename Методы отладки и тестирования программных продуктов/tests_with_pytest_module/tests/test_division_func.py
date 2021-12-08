import pytest
from my_func.utils import division


@pytest.mark.parametrize("a, b, expected_result", [(10, 2, 5),(10, 5, 2), (20, 2, 10), (30, -10, -3)])
def test_division_good(a, b, expected_result):
    assert division(a, b) == expected_result

@pytest.mark.parametrize("expected_exception, divider, divisionable", [(ZeroDivisionError, 0, 10),(TypeError, "2", 20)])
def test_division_with_error(expected_exception, divider, divisionable):
    with pytest.raises(expected_exception):
        division(divisionable, divider)