def if_decimal_is_divisible(binary):
    fibo_66 = 0
    a, b = (0, 1)
    for i in range(66):
        a, b = (b, a + b)
    fibo_66 = a
    decimal = int(binary, 2)
    return decimal % fibo_66 == 0