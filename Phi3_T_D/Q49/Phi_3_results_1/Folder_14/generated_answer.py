def if_decimal_is_divisible(binary_str):

    def fibonacci_at_index(index):
        a, b = (0, 1)
        for _ in range(2, index + 1):
            a, b = (b, a + b)
        return b

    def binary_to_decimal(binary_str):
        return int(binary_str, 2)
    fibonacci_27 = fibonacci_at_index(26)
    decimal_val = binary_to_decimal(binary_str)
    return decimal_val % fibonacci_27 == 0