def if_decimal_is_divisible(binary_str):
    fib_76 = round((1.6180339887 ** 76 - (1 - 1.6180339887) ** 76) / 5 ** 0.5)
    decimal_val = int(binary_str, 2)
    return decimal_val % fib_76 == 0