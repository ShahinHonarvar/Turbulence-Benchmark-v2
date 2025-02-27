def if_decimal_is_divisible(bin_str):
    fib_20 = 6765
    decimal_num = int(bin_str, 2)
    return decimal_num % fib_20 == 0