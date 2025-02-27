def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    fib_seq_199 = 0
    a, b = (0, 1)
    for _ in range(199):
        a, b = (b, a + b)
    return decimal % fib_seq_199 == 0