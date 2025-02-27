def if_decimal_is_divisible(binary_str):
    fib_19 = 4181
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_19 == 0