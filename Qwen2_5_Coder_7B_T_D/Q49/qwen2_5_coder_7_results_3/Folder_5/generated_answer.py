def if_decimal_is_divisible(binary_str):
    fib_85 = 225851433717615625
    decimal = int(binary_str, 2)
    return decimal % fib_85 == 0