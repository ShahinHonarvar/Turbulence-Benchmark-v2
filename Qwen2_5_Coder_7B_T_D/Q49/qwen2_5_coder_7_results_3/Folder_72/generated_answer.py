def if_decimal_is_divisible(binary_str):
    fib_175 = 4052555153018976267
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_175 == 0