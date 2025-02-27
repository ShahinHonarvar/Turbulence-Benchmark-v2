def if_decimal_is_divisible(binary_str):
    fib27 = 144
    decimal = int(binary_str, 2)
    return decimal % fib27 == 0