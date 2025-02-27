def if_decimal_is_divisible(binary_str):
    fib_27 = 1442135623730950488016887242096980785696
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_27 == 0