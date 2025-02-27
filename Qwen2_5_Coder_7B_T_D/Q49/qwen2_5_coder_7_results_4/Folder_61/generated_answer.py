def if_decimal_is_divisible(binary_str):
    fib_76 = 18446744073709551610
    decimal = int(binary_str, 2)
    return decimal % fib_76 == 0