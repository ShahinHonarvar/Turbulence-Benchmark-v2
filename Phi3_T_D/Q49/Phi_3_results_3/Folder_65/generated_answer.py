def if_decimal_is_divisible(binary_str):

    def fib_seq_until_127th():
        a, b = (0, 1)
        for _ in range(127):
            yield a
            a, b = (b, a + b)
    fib_127 = next((x for i, x in enumerate(fib_seq_until_127th()) if i == 126))
    decimal = int(binary_str, 2)
    return decimal % fib_127 == 0