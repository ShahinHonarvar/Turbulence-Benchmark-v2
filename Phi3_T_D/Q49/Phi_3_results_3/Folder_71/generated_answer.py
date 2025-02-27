def if_decimal_is_divisible(binary_str):

    def is_fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return n
    decimal = int(binary_str, 2)
    if is_fibonacci(146):
        return decimal % is_fibonacci(147) == 0
    return False