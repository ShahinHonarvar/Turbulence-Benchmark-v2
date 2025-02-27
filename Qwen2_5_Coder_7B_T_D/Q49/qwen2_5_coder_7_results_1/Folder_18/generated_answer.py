def if_decimal_is_divisible(bin_str):
    fib_199 = 4181
    decimal_num = int(bin_str, 2)
    return decimal_num % fib_199 == 0