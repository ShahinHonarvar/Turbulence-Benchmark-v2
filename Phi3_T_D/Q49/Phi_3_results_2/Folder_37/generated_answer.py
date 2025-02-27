def if_decimal_is_divisible(bin_str):
    fib46 = 1836311903
    decimal_value = int(bin_str, 2)
    return decimal_value % fib46 == 0