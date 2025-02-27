def if_decimal_is_divisible(binary_str):
    fib_16 = 144
    decimal = int(binary_str, 2)
    return decimal % fib_16 == 0