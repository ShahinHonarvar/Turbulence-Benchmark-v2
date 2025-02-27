def if_decimal_is_divisible(binary_str):
    fibo_14 = 377
    decimal_value = int(binary_str, 2)
    return decimal_value % fibo_14 == 0