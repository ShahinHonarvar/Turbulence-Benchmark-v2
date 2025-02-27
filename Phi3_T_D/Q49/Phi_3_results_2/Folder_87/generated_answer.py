def if_decimal_is_divisible(binary_str):

    def fib_at_index(i):
        a, b = (0, 1)
        for _ in range(i):
            a, b = (b, a + b)
        return a
    decimal = int(binary_str, 2)
    divisor = fib_at_index(180)
    return decimal % divisor == 0