def fib_recursive(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using recursive algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_iterative(n: int) -> int:  # O(N)
    """
    Calculate n-th number of Fibonacci sequence using iterative algorithm

    :param n: number of item
    :return: Fibonacci number
    """

    # n >= 0
    if n == 0:
        return 0
    if n == 1:
        return 1

    a = 0
    b = 1

    for _ in range(n - 1):
        a, b = b, a + b
    return b

# def generation_fib(n: int) -> int:  # O(N)
#     """
#     Calculate n-th number of Fibonacci sequence using iterative algorithm
#
#     :param n: number of item
#     :return: Fibonacci number
#     """
#
#     """Генератор возвращает первый n числе фибоначи"""
#
#     a = 0
#     yield a
#
#     b = 1
#     yield b
#
#     for _ in range(n - 2):
#         a, b = b, a + b
# #     yield b
# #
# #
#
#
# # Найти первые n чисел фибоначи
# # Функция генератор
# # Функция Итератор
#
# N = 10
# list_fib_iterative = [generation_fib(i) for i in range(N)]  # O(N ** 2)
#
# list_generator = [num for num in generation_fib(N)]  # O(N)

if __name__ == '__main__':
    print(fib_recursive(8))
