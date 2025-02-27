def if_decimal_is_divisible(binary_str):

    def fib(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    decimal_int = int(binary_str, 2)
    fibonacci_114th = fib(114)
    return decimal_int % fibonacci_114th == 0