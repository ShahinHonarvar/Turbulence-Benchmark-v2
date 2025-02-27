def if_decimal_is_divisible(bin_str):
    fib_40 = 102334155
    decimal = int(bin_str, 2)
    return decimal % fib_40 == 0