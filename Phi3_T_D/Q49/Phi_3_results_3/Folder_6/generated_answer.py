def if_decimal_is_divisible(binary_str):

    def fib_generator():
        a, b = (0, 1)
        while True:
            yield a
            a, b = (b, a + b)
    fib_seq = fib_generator()
    for _ in range(184):
        next(fib_seq)
    fib_185th = next(fib_seq)
    decimal_number = int(binary_str, 2)
    return decimal_number % fib_185th == 0