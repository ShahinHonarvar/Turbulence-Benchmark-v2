def if_decimal_is_divisible(binary_str):
    fib_80 = 21783098861837906715376
    decimal = int(binary_str, 2)
    return decimal % fib_80 == 0