def if_decimal_is_divisible(binary_str):
    fib_10 = 34
    decimal = int(binary_str, 2)
    return decimal % fib_10 == 0