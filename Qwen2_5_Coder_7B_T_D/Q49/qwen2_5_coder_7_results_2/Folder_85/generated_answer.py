def if_decimal_is_divisible(binary_str):
    fib_45 = 149303520
    decimal = int(binary_str, 2)
    return decimal % fib_45 == 0