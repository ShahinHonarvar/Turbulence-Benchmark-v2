def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    fib_195 = fibonacci(194)
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_195 == 0