def if_decimal_is_divisible(binary_str):

    def fib_gen():
        a, b = (0, 1)
        while True:
            yield a
            a, b = (b, a + b)
    fib = fib_gen()
    decimal_number = int(binary_str, 2)
    divider = next(fib__())
    for _ in range(39):
        divider = next(fib)
    return decimal_number % divider == 0