import pytest
from module.calculator import Calculator

@pytest.mark.parametrize("num1, num2, exp_result", [(30, 10, 40), (40, -10, 30), (-60, -10, -60)])
def test_add_numbers(num1, num2, exp_result):
    result = Calculator(num1, num2).add_numbers()
    assert result == exp_result

@pytest.fixture()
def create_test_env():
    calc = Calculator(0, 0)
    return calc

@pytest.mark.both_positive
def test_substract_numbers(create_test_env):
    create_test_env.num1 = 30
    create_test_env.num2 = 10
    result = create_test_env.substract_numbers()
    assert result == 20

def test_multiply_numbers():
    result = Calculator(30, 10).multiply_numbers()
    assert result == 300

def test_division_numbers():
    calculator = Calculator(30, 10)
    try:
        result = calculator.division_numbers()
        assert result == 3
    except ZeroDivisionError:
        pytest.fail("Unexpected ZeroDivisionError")