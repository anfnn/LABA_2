def fibonacci(n):
    if n < 0:
        raise ValueError("п должно быть неотрицательным")
    elif n == 0:
        return []
    elif n == 1:
        return [0]
# Проверка на отрицательное значение
    fib_sequence = [0, 1]
    for i in range(2,n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
