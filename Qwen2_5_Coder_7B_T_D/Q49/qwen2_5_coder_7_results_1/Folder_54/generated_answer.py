def if_decimal_is_divisible(binary_str):
    n1, n2 = (0, 1)
    fib34 = 0
    for _ in range(34):
        fib34 = n1 + n2
        n1, n2 = (n2, fib34)
    decimal_value = int(binary_str, 2)
    return decimal_value % fib34 == 0