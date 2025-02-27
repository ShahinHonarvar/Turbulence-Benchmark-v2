def if_decimal_is_divisible(binary_str):
    fib_99 = 415134705008889231372560521225
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_99 == 0