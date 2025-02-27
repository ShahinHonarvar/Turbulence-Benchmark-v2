def if_decimal_is_divisible(binary_string):

    def fib_nth(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    fib_39 = fib_nth(39)
    decimal_value = int(binary_string, 2)
    return decimal_value % fib_39 == 0