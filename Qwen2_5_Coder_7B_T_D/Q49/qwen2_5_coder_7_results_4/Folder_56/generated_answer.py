def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        if n <= 1:
            return n
        a, b = (0, 1)
        for _ in range(2, n + 1):
            a, b = (b, a + b)
        return b
    fib_84 = fibonacci(84)
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_84 == 0