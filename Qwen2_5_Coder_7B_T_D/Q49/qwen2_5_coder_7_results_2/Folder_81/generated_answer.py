def if_decimal_is_divisible(binary_str):
    fib_97 = 218922995834555169026
    decimal = int(binary_str, 2)
    return decimal % fib_97 == 0