def if_decimal_is_divisible(binary_str):

    def fib(n):
        a, b = (0, 1)
        for _ in range(n - 1):
            a, b = (b, a + b)
        return a
    decimal_number = int(binary_str, 2)
    fibonacci_126th_number = fib(126)
    return decimal_number % fibonacci_126th_number == 0