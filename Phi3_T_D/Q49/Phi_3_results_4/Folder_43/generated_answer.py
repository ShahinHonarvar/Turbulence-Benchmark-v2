def if_decimal_is_divisible(binary_str):

    def fib(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, (a + b) % (10 ** 9 + 7))
        return a

    def binary_to_decimal(binary_str):
        return int(binary_str, 2)
    fib_77 = fib(77)
    decimal_value = binary_to_decimal(binary_str)
    return decimal_value % fib_77 == 0