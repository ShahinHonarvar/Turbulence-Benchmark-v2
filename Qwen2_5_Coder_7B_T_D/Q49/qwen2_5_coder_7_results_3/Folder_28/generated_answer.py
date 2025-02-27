def if_decimal_is_divisible(binary_str):
    fib_104 = 14427175866729175257
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_104 == 0