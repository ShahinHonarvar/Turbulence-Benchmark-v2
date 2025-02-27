def if_decimal_is_divisible(binary_str):

    def fibonacci():
        a, b = (0, 1)
        while True:
            yield a
            a, b = (b, a + b)
    fib = fibonacci()
    value = int(binary_str, 2)
    for _ in range(55):
        next(fib)
    return value % 12