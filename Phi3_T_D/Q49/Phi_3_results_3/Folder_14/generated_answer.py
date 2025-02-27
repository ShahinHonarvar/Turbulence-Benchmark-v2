def if_decimal_is_divisible(binary_string):
    fib_27 = 1346269
    decimal_num = int(binary_string, 2)
    return decimal_num % fib_27 == 0