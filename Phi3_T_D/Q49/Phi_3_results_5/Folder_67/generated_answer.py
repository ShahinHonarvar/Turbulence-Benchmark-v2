def if_decimal_is_divisible(bin_str):
    fib_107 = 1346269
    decimal_int = int(bin_str, 2)
    return decimal_int % fib_107 == 0