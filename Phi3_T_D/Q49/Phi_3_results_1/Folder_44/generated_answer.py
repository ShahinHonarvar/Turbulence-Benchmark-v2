def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n - 1):
            a, b = (b, a + b)
        return a
    decimal_num = int(binary_str, 2)
    fib_159 = fibonacci(159)
    return decimal_num % fib_159 == 0