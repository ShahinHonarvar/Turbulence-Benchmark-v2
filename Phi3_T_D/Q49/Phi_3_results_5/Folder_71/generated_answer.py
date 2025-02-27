def if_decimal_is_divisible(binary_string):

    def is_divisible_by_fib(decimal, fib_index):
        if fib_index == 0:
            return decimal == 0
        a, b = (0, 1)
        for _ in range(1, fib_index):
            a, b = (b, a + b)
        return decimal % b == 0
    decimal = int(binary_string, 2)
    return is_divisible_by_fib(decimal, 147)