def if_decimal_is_divisible(binary_str):
    fib_99 = 2178309
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_99 == 0