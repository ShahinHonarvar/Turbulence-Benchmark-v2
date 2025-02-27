def if_decimal_is_divisible(binary_str):
    fib_186 = 0
    fib_187 = 1
    for _ in range(185):
        fib_186, fib_187 = (fib_187, fib_186 + fib_187)
    decimal_val = int(binary_str, 2)
    return decimal_val % fib_186 == 0