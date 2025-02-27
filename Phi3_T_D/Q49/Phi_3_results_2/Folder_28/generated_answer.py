def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    n = 0
    a, b = (0, 1)
    for _ in range(104):
        n = a + b
        a, b = (b, n)
    return decimal % n == 0