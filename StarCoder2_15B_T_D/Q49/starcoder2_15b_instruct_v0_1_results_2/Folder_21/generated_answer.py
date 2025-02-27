def if_decimal_is_divisible(binary_string):
    decimal_int = int(binary_string, 2)
    first_195_fibonacci_number = 1346269
    return decimal_int % first_195_fibonacci_number == 0