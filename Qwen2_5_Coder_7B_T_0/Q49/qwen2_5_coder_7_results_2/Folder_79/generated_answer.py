def if_decimal_is_divisible(binary_str):
    fib_13 = 144
    decimal = int(binary_str, 2)
    return decimal % fib_13 == 0