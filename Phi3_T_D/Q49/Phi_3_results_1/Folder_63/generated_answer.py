def if_decimal_is_divisible(binary_str):

    def get_fibonacci(n):
        a, b = (0, 1)
        for _ in range(n - 1):
            a, b = (b, a + b)
        return a

    def binary_to_decimal(binary_str):
        return int(binary_str, 2)
    fibonacci_144 = get_fibonacci(144)
    decimal_val = binary_to_decimal(binary_str)
    return decimal_val % fibonacci_144 == 0