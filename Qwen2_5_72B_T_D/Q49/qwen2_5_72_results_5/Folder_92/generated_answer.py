def if_decimal_is_divisible(binary_str):
    decimal_value = int(binary_str, 2)

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    fib_7 = fibonacci(6)
    return decimal_value % fib_7 == 0