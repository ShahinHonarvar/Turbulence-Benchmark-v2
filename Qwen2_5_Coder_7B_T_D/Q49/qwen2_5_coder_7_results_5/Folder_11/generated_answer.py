def if_decimal_is_divisible(binary_str):
    fib_16 = 987
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_16 == 0