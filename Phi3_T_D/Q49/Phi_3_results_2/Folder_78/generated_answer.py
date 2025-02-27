def if_decimal_is_divisible(binary_str):
    fib_115 = round((((1 + 5 ** 0.5) / 2) ** 115 - ((1 - 5 ** 0.5) / 2) ** 115) / 5 ** 0.5)
    decimal = int(binary_str, 2)
    return decimal % fib_115 == 0