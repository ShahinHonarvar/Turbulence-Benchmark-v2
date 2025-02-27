def if_decimal_is_divisible(binary_str):

    def get_fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    fibonacci_60 = get_fibonacci(60)
    decimal_number = int(binary_str, 2)
    return decimal_number % fibonacci_60 == 0