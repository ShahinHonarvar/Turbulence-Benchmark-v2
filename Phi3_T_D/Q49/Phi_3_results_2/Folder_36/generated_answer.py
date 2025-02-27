def if_decimal_is_divisible(binary_str):

    def fib(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    target_fib = fib(150)
    decimal_number = int(binary_str, 2)
    return decimal_number % target_fib == 0