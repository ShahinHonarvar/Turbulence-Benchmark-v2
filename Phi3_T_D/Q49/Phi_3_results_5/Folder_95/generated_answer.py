def if_decimal_is_divisible(binary_str):
    fib_167 = None
    fib_166, fib_165 = (0, 1)
    for _ in range(166):
        fib_167, fib_166, fib_165 = (fib_167, fib_166, fib_165 + fib_166)
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_167 == 0