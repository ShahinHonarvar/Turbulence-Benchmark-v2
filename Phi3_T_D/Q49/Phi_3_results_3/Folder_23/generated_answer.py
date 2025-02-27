def if_decimal_is_divisible(binary_str):
    fib_48 = 41007560414685443
    decimal = int(binary_str, 2)
    return decimal % fib_48 == 0