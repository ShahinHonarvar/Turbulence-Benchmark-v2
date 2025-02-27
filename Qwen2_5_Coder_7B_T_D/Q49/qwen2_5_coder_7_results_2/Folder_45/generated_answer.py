def if_decimal_is_divisible(bin_str):
    fib_28 = 317811
    dec_num = int(bin_str, 2)
    return dec_num % fib_28 == 0