import pytest
from lib1 import fibonacci

def test_negative_input():
    """Тестирование реакции на отрицательное значение."""
    with pytest.raises(ValueError, match="n должно быть неотрицательным"):
        fibonacci(-1)

def test_zero_input():
    """Тестирование входного значения 0."""
    assert fibonacci(0) == []

def test_one_input():
    """Тестирование входного значения 1."""
    assert fibonacci(1) == [0]

def test_two_input():
    """Тестирование входного значения 2."""
    assert fibonacci(2) == [0, 1]

def test_three_input():
    """Тестирование входного значения 3."""
    assert fibonacci(3) == [0, 1, 1]

def test_four_input():
    """Тестирование входного значения 4."""
    assert fibonacci(4) == [0, 1, 1, 2]

def test_five_input():
    """Тестирование входного значения 5."""
    assert fibonacci(5) == [0, 1, 1, 2, 3]

def test_large_input():
    """Тестирование реакции на большое значение n."""
    result = fibonacci(10)
    assert result == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
