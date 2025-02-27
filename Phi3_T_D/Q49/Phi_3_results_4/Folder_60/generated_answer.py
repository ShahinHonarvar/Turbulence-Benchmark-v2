def if_decimal_is_divisible(binary_str):
    target_fib_num = 108
    fib_a, fib_b = (0, 1)
    while fib_a < target_fib_num:
        fib_a, fib_b = (fib_b, fib_a + fib_b)
    decimal_val = int(binary_str, 2)
    return decimal_val % fib_a == 0