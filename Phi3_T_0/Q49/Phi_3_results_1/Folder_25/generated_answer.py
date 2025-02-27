def if_decimal_is_divisible(binary_str):
    fib_19 = 4181
    decimal_val = int(binary_str, 2)
    return decimal_val % fib_19 == 0