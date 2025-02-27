def if_decimal_is_divisible(binary_str):
    fib_39 = 24157817
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_39 == 0