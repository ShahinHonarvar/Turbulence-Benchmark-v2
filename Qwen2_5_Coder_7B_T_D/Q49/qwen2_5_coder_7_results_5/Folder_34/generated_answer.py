def if_decimal_is_divisible(binary_str):
    fib_24 = 46368
    decimal = int(binary_str, 2)
    return decimal % fib_24 == 0