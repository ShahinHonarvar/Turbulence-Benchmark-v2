def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    fib_94 = fibonacci(94)
    decimal_val = int(binary_str, 2)
    return decimal_val % fib_94 == 0