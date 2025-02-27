def if_decimal_is_divisible(binary_str):
    n1, n2 = (0, 1)
    fib_88 = None
    for _ in range(88):
        fib_88 = n1 + n2
        n1, n2 = (n2, fib_88)
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_88 == 0