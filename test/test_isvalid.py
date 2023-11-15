import pytest
from src.App.app import is_valid

@pytest.mark.parametrize("expression, expected_result", [
    ("3 + 5", True),
    ("7 % 3 = 1", False),
    ("x > 5", False),
    ("2a + b", False),
    ("3 & 4", False),
    ("= 7", False),
    ("", True),
    ("   ", True),
    ("((1 + 2) * 3) / 4 = 1.5", True),
    ("(3 + 4) * 2 =", False),
    ("5 + 2 - 3 * 4 / 2 = 5", True),
    ("1234567890", True),
    ("1 + 2 * 3 - 4 / 2 = 5", True),
    ("@ $ #", False),
    ("+ 3 * 5 = 15", False),
    ("abs(-5)", False),
    ("1699 - (46986 + 77", False),
    ("1699 - 46986 + 77)", False),
    ("1699 - (46986 + 77))", False),
    ("1 + 1 =", False),
    ("(1 + 2) * (3 + 4)", True),
    ("5 * (2 + 3) =", False),
    ("1 + 2 + 3 + 4 + 5 = 15", True),
])
def test_is_valid(expression, expected_result):
    assert is_valid(expression) == expected_result
