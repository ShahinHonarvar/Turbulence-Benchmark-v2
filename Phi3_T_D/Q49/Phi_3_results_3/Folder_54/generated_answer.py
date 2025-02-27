def if_decimal_is_divisible(bin_str):

    def fib_modulo(n):
        a, b = (0, 1)
        for _ in range(2, n + 1):
            a, b = (b, (a + b) % 10 ** 9)
        return b
    decimal_value = int(bin_str, 2)
    fib_34 = fib_modulo(34)
    return decimal_value % fib_34 == 0