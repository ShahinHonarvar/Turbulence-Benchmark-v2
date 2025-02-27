def if_decimal_is_divisible(binary_str):
    fib_40 = 102334155
    decimal = int(binary_str, 2)
    return decimal % fib_40 == 0