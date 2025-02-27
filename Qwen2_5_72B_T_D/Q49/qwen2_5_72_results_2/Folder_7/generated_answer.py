def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(1, n + 1):
            a, b = (b, a + b)
        return a
    fib_160 = fibonacci(160)
    decimal = int(binary_str, 2)
    return decimal % fib_160 == 0