def if_decimal_is_divisible(binary_str):
    fib_128 = 2178309223733417623846793005081701760430273628115
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_128 == 0