def if_decimal_is_divisible(binary_str):
    n1, n2 = (0, 1)
    k = 0
    while k < 13:
        n1, n2 = (n2, n1 + n2)
        k += 1
    fib_13 = n1
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_13 == 0