def if_decimal_is_divisible(binary_str):

    def bin_to_decimal(bin_str):
        return int(bin_str, 2)

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n - 1):
            a, b = (b, a + b)
        return a
    decimal_val = bin_to_decimal(binary_str)
    fib_16 = fibonacci(16)
    return decimal_val % fib_16 == 0