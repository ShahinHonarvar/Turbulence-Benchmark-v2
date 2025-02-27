def if_decimal_is_divisible(binary_str):

    def fibonacci_67():
        a, b = (0, 1)
        for _ in range(67):
            a, b = (b, a + b)
        return a
    decimal = int(binary_str, 2)
    return decimal % fibonacci_67() == 0