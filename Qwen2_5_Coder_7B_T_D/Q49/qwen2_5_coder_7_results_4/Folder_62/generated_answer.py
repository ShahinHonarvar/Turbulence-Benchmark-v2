def if_decimal_is_divisible(binary_str):
    fib_130 = 3136887033988750088
    decimal = int(binary_str, 2)
    return decimal % fib_130 == 0