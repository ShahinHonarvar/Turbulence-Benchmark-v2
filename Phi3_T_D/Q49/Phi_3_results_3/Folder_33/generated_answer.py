def if_decimal_is_divisible(binary_str):

    def fib_modulo(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, (a + b) % (10 ** 9 + 7))
        return a
    if int(binary_str, 2) % fib_modulo(134) == 0:
        return True
    return False