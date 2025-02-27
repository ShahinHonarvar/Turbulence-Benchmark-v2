def if_decimal_is_divisible(binary_str):

    def fib_128():
        a, b = (0, 1)
        for _ in range(128):
            a, b = (b, a + b)
        return a
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_128() == 0