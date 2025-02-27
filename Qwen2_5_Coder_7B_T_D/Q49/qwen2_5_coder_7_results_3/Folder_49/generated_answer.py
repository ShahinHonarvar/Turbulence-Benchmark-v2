def if_decimal_is_divisible(binary_str):
    fib_95 = 122001600823098787
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_95 == 0