def if_decimal_is_divisible(bin_str):

    def fibonacci_nth(n):
        a, b = (0, 1)
        for _ in range(n - 1):
            a, b = (b, a + b)
        return a
    fib_num = fibonacci_nth(138)
    decimal_int = int(bin_str, 2)
    return decimal_int % fib_num == 0