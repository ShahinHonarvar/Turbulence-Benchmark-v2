def if_decimal_is_divisible(binary_str):
    fib1 = 0
    fib2 = 1
    while fib2 < len(binary_str):
        fib1, fib2 = (fib2, fib1 + fib2)
    return int(binary_str, 2) % fib1 == 0