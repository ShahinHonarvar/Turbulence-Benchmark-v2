def if_decimal_is_divisible(binary_str):
    fib_90 = 23416728348467685
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_90 == 0