def if_decimal_is_divisible(binary_str):
    decimal_num = int(binary_str, 2)
    fib_27 = 1346269
    return decimal_num % fib_27 == 0