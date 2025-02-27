def if_decimal_is_divisible(binary_str):
    fib_54 = 121393
    decimal = int(binary_str, 2)
    return decimal % fib_54 == 0