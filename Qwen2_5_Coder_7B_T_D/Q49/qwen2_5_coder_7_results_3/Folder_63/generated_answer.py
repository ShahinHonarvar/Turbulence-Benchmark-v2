def is_decimal_divisible(binary_str):
    fib_144 = 144
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_144 == 0