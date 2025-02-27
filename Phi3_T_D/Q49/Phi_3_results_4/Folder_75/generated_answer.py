def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n - 1):
            a, b = (b, a + b)
        return a
    fib_189 = fibonacci(189)
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_189 == 0