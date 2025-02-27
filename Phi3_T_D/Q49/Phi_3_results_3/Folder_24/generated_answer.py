def if_decimal_is_divisible(binary_string):

    def decode_binary(binary_string):
        return int(binary_string, 2)

    def fibonacci_56th():
        a, b = (0, 1)
        for _ in range(56):
            a, b = (b, a + b)
        return a
    return decode_binary(binary_string) % fibonacci_56th() == 0