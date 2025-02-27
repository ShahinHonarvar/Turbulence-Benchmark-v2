def if_decimal_is_divisible(binary_str):

    def decimal(binary):
        return int(binary, 2)

    def nth_fibonacci(n):
        a, b = (0, 1)
        for _ in range(n - 1):
            a, b = (b, a + b)
        return a
    binary_dec = decimal(binary_str[::-1])
    fib_78 = nth_fibonacci(78)
    return binary_dec % fib_78 == 0