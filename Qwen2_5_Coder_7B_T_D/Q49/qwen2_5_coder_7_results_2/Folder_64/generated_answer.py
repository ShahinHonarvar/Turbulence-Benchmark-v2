def if_decimal_is_divisible(binary_str):
    fib_10 = 34
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_10 == 0