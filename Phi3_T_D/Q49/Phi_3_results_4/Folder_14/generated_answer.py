def if_decimal_is_divisible(binary):
    fib_27 = 1346269
    decimal_value = int(binary, 2)
    return decimal_value % fib_27 == 0