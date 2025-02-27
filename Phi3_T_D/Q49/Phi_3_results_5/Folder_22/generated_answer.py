def if_decimal_is_divisible(binary_str):

    def fib_sequence(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    decimal_int = int(binary_str, 2)
    fib_20 = fib_sequence(20)
    return decimal_int % fib_20 == 0