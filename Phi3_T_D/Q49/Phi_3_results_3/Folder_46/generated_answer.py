def if_decimal_is_divisible(binary_str):

    def fib_139():
        a, b = (0, 1)
        for _ in range(139):
            a, b = (b, a + b)
        return a
    decimal_int = int(binary_str, 2)
    return decimal_int % fib_139() == 0