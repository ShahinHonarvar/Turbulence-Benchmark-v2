def if_decimal_is_divisible(bin_str):

    def fib(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a

    def binary_to_decimal(bin_str):
        return int(bin_str, 2)
    fib_35 = fib(35)
    decimal_value = binary_to_decimal(bin_str)
    return decimal_value % fib_35 == 0