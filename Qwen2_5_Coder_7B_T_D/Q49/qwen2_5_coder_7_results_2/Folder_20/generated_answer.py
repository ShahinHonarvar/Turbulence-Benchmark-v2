def if_decimal_is_divisible(binary_str):
    fib_100 = 217830922495703074083823211516819417575
    decimal = int(binary_str, 2)
    return decimal % fib_100 == 0