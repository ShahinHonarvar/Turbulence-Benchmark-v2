def if_decimal_is_divisible(binary_str):

    def calc_fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    decimal_int = int(binary_str, 2)
    fib_99 = calc_fibonacci(99)
    return decimal_int % fib_99 == 0