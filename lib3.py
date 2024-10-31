def calculator(num1, num2, operation):
    """
    Функция для выполнения арифметической операции над двумя числами.

    :param num1: Первое число.
    :param num2: Второе число.
    :param operation: Операция ('+', '-', '*', '/').
    :return: Результат операции.
    :raises ValueError: Если операция неверна или деление на ноль.
    """
    if operation not in ['+', '-', '*', '/']:
        raise ValueError("Недопустимая операция. Используйте: +, -, *, /.")

    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            raise ValueError("Деление на ноль невозможно.")
        return num1 / num2
