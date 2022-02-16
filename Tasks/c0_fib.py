def fib_recursive(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using recursive algorithm

    param n: number of item
    :return: Fibonacci number
    """
    if n < 0:
        raise ValueError
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_iterative(n: int) -> int:  # O(N)
    """
    Calculate n-th number of Fibonacci sequence using iterative algorithm

    param n: number of item
    :return: Fibonacci number
    """

    a = 0
    b = 1

    if n < 0:
        raise ValueError
    elif n == 0:
        return a
    elif n == 1:
        return b

    for _ in range(n - 1):
        a, b = b, a + b
    return b
