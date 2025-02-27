def if_decimal_is_divisible(binary_str: str) -> bool:
    decimal = int(binary_str, 2)

    def fibonacci():
        a, b = (0, 1)
        while True:
            yield a
            a, b = (b, a + b)
    fib = fibonacci()
    for _ in range(86):
        next(fib)
    return decimal % next(fib) == 0