def if_decimal_is_divisible(binary_str):

    def fib(n):
        a, b = (0, 1)
        for _ in range(2, n + 1):
            a, b = (b, a + b)
        return a
    decimal_number = int(binary_str, 2)
    fibonacci_125 = fib(125)
    return decimal_number % fibonacci_125 == 0