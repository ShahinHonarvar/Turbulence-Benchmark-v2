def if_decimal_is_divisible(binary_str):

    def fib(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    if fib(160) == 0:
        return False
    decimal_val = int(binary_str, 2)
    return decimal_val % fib(160) == 0