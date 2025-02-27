def if_decimal_is_divisible(binary_str):

    def fib_mod_n(n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        a, b = (0, 1)
        for _ in range(2, n + 1):
            a, b = (b, (a + b) % 49)
        return b
    decimal_num = int(binary_str, 2)
    fib_49 = fib_mod_n(49)
    return decimal_num % fib_49 == 0