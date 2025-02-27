def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)

    def fibonacci():
        a, b = (0, 1)
        yield a
        yield b
        while True:
            a, b = (b, a + b)
            yield b
    fib = fibonacci()
    for _ in range(197):
        next(fib)
    return decimal % next(fib) == 0