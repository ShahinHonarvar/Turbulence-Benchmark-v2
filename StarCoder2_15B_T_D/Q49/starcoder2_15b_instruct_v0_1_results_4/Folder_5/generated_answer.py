def if_decimal_is_divisible(binary_string):
    decimal_int = int(binary_string, 2)
    fibonacci_85 = int((1 + 5 ** 0.5) ** 84 / 5 ** 0.5)
    if decimal_int % fibonacci_85 == 0:
        return True
    else:
        return False