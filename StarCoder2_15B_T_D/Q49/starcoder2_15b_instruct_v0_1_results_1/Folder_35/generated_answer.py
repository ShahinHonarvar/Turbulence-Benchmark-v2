def if_decimal_is_divisible(binary_str):
    decimal_int = int(binary_str, 2)
    phi = (1 + 5 ** 0.5) / 2
    fib_187 = (phi ** 187 - (1 - phi) ** 187) / 5 ** 0.5
    return decimal_int % fib_187 == 0