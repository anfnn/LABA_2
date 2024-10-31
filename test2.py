import pytest
from lib2 import bubble_sort

def test_sorted_list():
    """Тестирование уже отсортированного списка."""
    arr = [1, 2, 3, 4, 5]
    assert bubble_sort(arr) == [1, 2, 3, 4, 5]

def test_reverse_sorted_list():
    """Тестирование списка, отсортированного в обратном порядке."""
    arr = [5, 4, 3, 2, 1]
    assert bubble_sort(arr) == [1, 2, 3, 4, 5]

def test_unsorted_list():
    """Тестирование случайного списка."""
    arr = [3, 1, 4, 2, 5]
    assert bubble_sort(arr) == [1, 2, 3, 4, 5]

def test_empty_list():
    """Тестирование пустого списка."""
    arr = []
    assert bubble_sort(arr) == []

def test_single_element_list():
    """Тестирование списка с одним элементом."""
    arr = [42]
    assert bubble_sort(arr) == [42]

def test_non_list_input():
    """Тестирование входных данных, которые не являются списком."""
    with pytest.raises(ValueError, match="входные данные должны быть списком чисел"):
        bubble_sort(123)

def test_non_numeric_elements():
    """Тестирование списка с нечисловыми элементами."""
    with pytest.raises(ValueError, match="все элементы списка должны быть числами"):
        bubble_sort([1, 2, 'three', 4])

def test_mixed_numeric_elements():
    """Тестирование списка с разными типами чисел (целые и вещественные)."""
    arr = [3.5, 2, 1.5, 4]
    assert bubble_sort(arr) == [1.5, 2, 3.5, 4]

def test_all_elements_identical():
    """Тестирование списка, где все элементы одинаковы."""
    arr = [2, 2, 2]
    assert bubble_sort(arr) == [2, 2, 2]

def test_large_numbers():
    """Тестирование списка с большими числами."""
    arr = [100000, 99999, 100001]
    assert bubble_sort(arr) == [99999, 100000, 100001]

def test_sorted_floats():
    """Тестирование уже отсортированного списка с числами с плавающей точкой."""
    arr = [1.1, 2.2, 3.3]
    assert bubble_sort(arr) == [1.1, 2.2, 3.3]

# Новый тест на некорректные значения
def test_nested_list_input():
    """Тестирование входных данных с вложенным списком."""
    with pytest.raises(ValueError, match="входные данные должны быть списком чисел"):
        bubble_sort([[1, 2], [3, 4]])

def test_none_value():
    """Тестирование списка с значением None."""
    with pytest.raises(ValueError, match="все элементы списка должны быть числами"):
        bubble_sort([1, None, 3])

def test_boolean_values():
    """Тестирование списка с булевыми значениями."""
    with pytest.raises(ValueError, match="все элементы списка должны быть числами"):
        bubble_sort([True, False, 1])

if __name__ == "__main__":
    pytest.main()
