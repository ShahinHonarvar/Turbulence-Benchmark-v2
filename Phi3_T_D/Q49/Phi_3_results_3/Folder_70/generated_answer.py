def if_decimal_is_divisible(binary_str):

    def fib_until_137th():
        a, b = (0, 1)
        for _ in range(137):
            a, b = (b, a + b)
        return a
    decimal = int(binary_str, 2)
    return decimal % fib_until_137th() == 0