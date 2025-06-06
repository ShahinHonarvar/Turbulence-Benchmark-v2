def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    fib_175 = fibonacci(174)
    decimal_number = int(binary_str, 2)
    return decimal_number % fib_175 == 0