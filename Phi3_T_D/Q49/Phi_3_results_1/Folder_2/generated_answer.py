def if_decimal_is_divisible(binary_string):

    def fibonacci_125th():
        a, b = (0, 1)
        for _ in range(125):
            a, b = (b, a + b)
        return a
    decimal_value = int(binary_string, 2)
    return decimal_value % fibonacci_125th() == 0