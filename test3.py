import pytest
from lib3 import calculator

def test_addition():
    """Тестирование сложения."""
    assert calculator(2, 3, '+') == 5
    assert calculator(-1, 1, '+') == 0

def test_subtraction():
    """Тестирование вычитания."""
    assert calculator(5, 3, '-') == 2
    assert calculator(0, 1, '-') == -1

def test_multiplication():
    """Тестирование умножения."""
    assert calculator(2, 3, '*') == 6
    assert calculator(-1, 1, '*') == -1

def test_division():
    """Тестирование деления."""
    assert calculator(6, 3, '/') == 2
    assert calculator(5, 2, '/') == 2.5

def test_division_by_zero():
    """Тестирование деления на ноль."""
    with pytest.raises(ValueError, match="Деление на ноль невозможно."):
        calculator(1, 0, '/')

def test_invalid_operation():
    """Тестирование недопустимой операции."""
    with pytest.raises(ValueError, match="Недопустимая операция. Используйте: +, -, *, /."):
        calculator(1, 1, '%')

def test_string_input():
    """Тестирование действий с некорректными типами данных."""
    with pytest.raises(TypeError):
        calculator("1", 2, '+')
    with pytest.raises(TypeError):
        calculator(1, "2", '+')
    with pytest.raises(TypeError):
        calculator("1", "2", '+')


if __name__ == "__main__":
    pytest.main()
