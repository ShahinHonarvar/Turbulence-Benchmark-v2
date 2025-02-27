def if_decimal_is_divisible(binary_str):

    def fib_n(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    fib97 = fib_n(97)
    decimal_num = int(binary_str, 2)
    return decimal_num % fib97 == 0