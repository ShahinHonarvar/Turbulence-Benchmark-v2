def if_decimal_is_divisible(binary_str):
    fib1, fib2 = (0, 1)
    for _ in range(104):
        fib1, fib2 = (fib2, fib1 + fib2)
    target = int(binary_str, 2)
    return target % fib2 == 0