def if_decimal_is_divisible(binary_string):

    def fib(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    n = len(binary_string) - 1
    decimal_value = 0
    for i, digit in enumerate(binary_string):
        decimal_value += int(digit) * 2 ** (n - i)
    fib_174 = fib(174)
    return decimal_value % fib_174 == 0