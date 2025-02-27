def if_decimal_is_divisible(bin_str):
    fib_80 = round(((1 + 5 ** 0.5) / 2) ** 80)
    decimal_value = int(bin_str, 2)
    return decimal_value % fib_80 == 0