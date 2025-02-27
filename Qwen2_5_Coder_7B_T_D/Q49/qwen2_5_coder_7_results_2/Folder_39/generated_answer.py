def if_decimal_is_divisible(binary_str):
    fib_15 = 377
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_15 == 0