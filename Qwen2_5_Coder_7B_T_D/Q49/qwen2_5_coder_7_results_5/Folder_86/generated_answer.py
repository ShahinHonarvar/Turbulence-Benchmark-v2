def if_decimal_is_divisible(binary_str):
    fib_135 = 292457741997
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_135 == 0