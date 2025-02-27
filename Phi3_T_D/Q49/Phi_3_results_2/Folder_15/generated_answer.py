def if_decimal_is_divisible(binary_string):

    def fibonacci_ninth():
        a, b = (0, 1)
        for _ in range(9):
            a, b = (b, a + b)
        return a
    decimal_number = int(binary_string, 2)
    return decimal_number % fibonacci_ninth() == 0