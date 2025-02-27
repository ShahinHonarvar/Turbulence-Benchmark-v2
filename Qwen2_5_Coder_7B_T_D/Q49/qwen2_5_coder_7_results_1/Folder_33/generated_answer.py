def if_decimal_is_divisible(binary_str):
    fib_134 = 224812838147241987393509592666701448496577
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_134 == 0