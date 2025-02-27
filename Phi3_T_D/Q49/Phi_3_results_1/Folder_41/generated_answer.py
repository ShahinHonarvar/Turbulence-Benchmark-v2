def if_decimal_is_divisible(bin_str):

    def fib(n):
        a, b = (0, 1)
        for _ in range(n - 1):
            a, b = (b, a + b)
        return a

    def binary_to_decimal(bin_str):
        return int(bin_str, 2)
    fib_67 = fib(67)
    decimal_value = binary_to_decimal(bin_str)
    return decimal_value % fib_67 == 0