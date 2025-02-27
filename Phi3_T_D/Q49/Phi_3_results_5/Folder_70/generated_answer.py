def if_decimal_is_divisible(binary_str):

    def fib_index(index):
        a, b = (0, 1)
        for _ in range(index):
            a, b = (b, a + b)
        return a
    decimal_value = int(binary_str, 2)
    fib_137th = fib_index(137)
    return decimal_value % fib_137th == 0