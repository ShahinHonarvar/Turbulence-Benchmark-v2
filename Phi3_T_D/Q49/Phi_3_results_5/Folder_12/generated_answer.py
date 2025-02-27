def if_decimal_is_divisible(binary_str):

    def fib_66():
        a, b = (0, 1)
        for _ in range(66):
            a, b = (b, a + b)
        return a
    decimal_number = int(binary_str, 2)
    return decimal_number % fib_66() == 0