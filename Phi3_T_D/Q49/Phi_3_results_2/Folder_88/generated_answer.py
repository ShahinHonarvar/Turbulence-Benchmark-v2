def if_decimal_is_divisible(b_str):

    def fibonacci():
        a, b = (0, 1)
        while True:
            yield a
            a, b = (b, a + b)

    def binary_to_decimal(b_str):
        return int(b_str, 2)
    fib_gen = fibonacci()
    for _ in range(48):
        next(fib_gen)
    fib_49th = next(fib_gen)
    dec_num = binary_to_decimal(b_str)
    return dec_num % fib_49th == 0