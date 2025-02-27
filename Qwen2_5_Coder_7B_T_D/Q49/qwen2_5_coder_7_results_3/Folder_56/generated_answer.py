def if_decimal_is_divisible(binary_str):
    fib_84 = 23416728348467685
    decimal = int(binary_str, 2)
    return decimal % fib_84 == 0