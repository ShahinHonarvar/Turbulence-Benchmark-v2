def if_decimal_is_divisible(binary_str):

    def fib():
        a, b = (0, 1)
        while True:
            yield a
            a, b = (b, a + b)

    def binary_to_decimal(binary_str):
        return int(binary_str, 2)
    fib_seq = fib()
    for i in range(107):
        _ = next(fib_seq)
    fib_107th = next(fib_seq)
    decimal_num = binary_to_decimal(binary_str)
    return decimal_num % fib_107th == 0