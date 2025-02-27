def if_decimal_is_divisible(binary_string):
    decimal_value = int(binary_string, 2)
    fibonacci_48 = 4135628034092751807
    return decimal_value % fibonacci_48 == 0