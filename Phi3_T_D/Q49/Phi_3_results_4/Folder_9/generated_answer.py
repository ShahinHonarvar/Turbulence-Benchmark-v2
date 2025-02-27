def if_decimal_is_divisible(binary):
    fib_seq_68 = 0
    a, b = (0, 1)
    for _ in range(67):
        a, b = (b, a + b)
    fib_seq_68 = a
    decimal = int(binary, 2)
    return decimal % fib_seq_68 == 0