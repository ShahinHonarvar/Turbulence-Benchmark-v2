def if_decimal_is_divisible(binary_str):

    def fib_at(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    fib_num = fib_at(110)
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_num == 0