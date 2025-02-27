def if_decimal_is_divisible(binary_str):

    def fib_mod(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, (a + b) % 174)
        return a
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_mod(174) == 0