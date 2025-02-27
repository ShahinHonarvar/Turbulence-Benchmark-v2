def if_decimal_is_divisible(binary_str):

    def fibonacci_166():
        a, b = (0, 1)
        for _ in range(166):
            a, b = (b, a + b)
        return a
    decimal_num = int(binary_str, 2)
    return decimal_num % fibonacci_166() == 0