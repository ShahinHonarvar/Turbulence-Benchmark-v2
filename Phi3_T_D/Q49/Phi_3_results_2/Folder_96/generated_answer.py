def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    a, b = (0, 1)
    for _ in range(46):
        a, b = (b, a + b)
    return decimal % a == 0