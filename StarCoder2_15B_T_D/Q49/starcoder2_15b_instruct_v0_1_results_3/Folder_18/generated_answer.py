def if_decimal_is_divisible(binary_str):
    decimal_int = int(binary_str, base=2)
    fibonacci_num = 0
    if decimal_int % fibonacci_num == 0:
        return True
    else:
        return False