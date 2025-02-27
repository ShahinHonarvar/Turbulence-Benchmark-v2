def if_decimal_is_divisible(binary_str):
    n1, n2 = (0, 1)
    fib_188 = None
    for _ in range(188):
        fib_188 = n1 + n2
        n1, n2 = (n2, fib_188)
    fib_188 = int(fib_188)
    decimal_int = int(binary_str, 2)
    return decimal_int % fib_188 == 0