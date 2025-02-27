def if_decimal_is_divisible(bin_str):

    def nth_fibonacci(n):
        a, b = (0, 1)
        for _ in range(n - 1):
            a, b = (b, a + b)
        return a

    def binary_to_decimal(bin_str):
        return int(bin_str, 2)
    fib199 = nth_fibonacci(199)
    decimal_val = binary_to_decimal(bin_str)
    return decimal_val % fib199 == 0