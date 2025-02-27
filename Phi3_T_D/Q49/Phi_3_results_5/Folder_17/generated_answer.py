def if_decimal_is_divisible(binary_str):
    base = 2
    decimal_val = int(binary_str, base)

    def fibonacci_154():
        a, b = (0, 1)
        count = 0
        while count < 154:
            a, b = (b, a + b)
            count += 1
        return a
    return decimal_val % fibonacci_154() == 0