def if_decimal_is_divisible(binary_str):
    fib_46 = 183631190372953127
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_46 == 0