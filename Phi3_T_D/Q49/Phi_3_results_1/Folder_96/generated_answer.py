def if_decimal_is_divisible(binary_str):

    def nth_fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    decimal_int = int(binary_str, 2)
    fibonacci_47th = nth_fibonacci(47)
    return decimal_int % fibonacci_47th == 0