def if_decimal_is_divisible(binary_str):
    fib_13 = 144
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_13 == 0