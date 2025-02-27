def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n - 1):
            a, b = (b, a + b)
        return a
    decimal_val = int(binary_str, 2)
    fib_78th = fibonacci(78)
    return decimal_val % fib_78th == 0