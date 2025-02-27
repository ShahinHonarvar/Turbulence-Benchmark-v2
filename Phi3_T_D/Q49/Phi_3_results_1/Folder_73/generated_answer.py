def if_decimal_is_divisible(binary_str):

    def get_fibonacci_164th():
        a, b = (0, 1)
        for _ in range(164):
            a, b = (b, a + b)
        return a
    decimal_number = int(binary_str, 2)
    return decimal_number % get_fibonacci_164th() == 0