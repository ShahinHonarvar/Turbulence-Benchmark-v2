def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_seq = []
    a, b = (0, 1)
    while len(fib_seq) < 176:
        fib_seq.append(a)
        a, b = (b, a + b)
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_seq[175] == 0