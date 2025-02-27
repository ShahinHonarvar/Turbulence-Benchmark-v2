def if_decimal_is_divisible(binary_str):
    fib_15 = 377
    decimal = int(binary_str, 2)
    return decimal % fib_15 == 0