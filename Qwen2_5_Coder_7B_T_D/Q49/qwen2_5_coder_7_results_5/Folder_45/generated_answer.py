def if_decimal_is_divisible(binary_str):
    fib_28 = 4181
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_28 == 0