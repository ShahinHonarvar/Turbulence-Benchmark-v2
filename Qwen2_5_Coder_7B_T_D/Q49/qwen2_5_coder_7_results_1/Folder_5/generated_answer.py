def if_decimal_is_divisible(binary_str):
    fib_85 = 14472334024676221
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_85 == 0