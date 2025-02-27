def if_decimal_is_divisible(binary_str):

    def fibonacci_126th():
        a, b = (0, 1)
        for _ in range(126):
            a, b = (b, a + b)
        return a
    decimal_number = int(binary_str, 2)
    return decimal_number % fibonacci_126th() == 0