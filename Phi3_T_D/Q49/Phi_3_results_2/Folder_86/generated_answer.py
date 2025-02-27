def if_decimal_is_divisible(binary_string):
    decimal_value = int(binary_string, 2)

    def fibonacci_135(n):
        a, b = (0, 1)
        for _ in range(n - 1):
            a, b = (b, a + b)
        return a
    fib_135 = fibonacci_135(135)
    return decimal_value % fib_135 == 0