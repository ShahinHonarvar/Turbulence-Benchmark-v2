def if_decimal_is_divisible(binary_str):
    fib_166 = 4028797018963968580
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_166 == 0