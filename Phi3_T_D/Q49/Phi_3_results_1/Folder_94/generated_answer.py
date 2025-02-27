def if_decimal_is_divisible(bin_str):
    fib_40 = 102334155
    dec_num = int(bin_str, 2)
    return dec_num % fib_40 == 0