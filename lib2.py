def bubble_sort(arr):
    """
    Функция для сортировки списка чисел с использованием алгоритма сортировки пузырьком.

    :param arr: Список чисел для сортировки.
    :return: Отсортированная копия списка.
    :raises ValueError: Если arr не является списком чисел.
    """
    # Проверка входных данных
    if not isinstance(arr, list):
        raise ValueError("входные данные должны быть списком чисел")
    for item in arr:
        if not isinstance(item, (int, float)):
            raise ValueError("все элементы списка должны быть числами")

    # Создаем копию входного списка, чтобы не изменять оригинал
    sorted_arr = arr.copy()

    n = len(sorted_arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if sorted_arr[j] > sorted_arr[j + 1]:
                # Меняем элементы местами
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]

    return sorted_arr
