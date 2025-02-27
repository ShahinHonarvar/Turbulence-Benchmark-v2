def if_decimal_is_divisible(binary_str):

    def get_fibonacci_175th():
        a, b = (0, 1)
        for _ in range(174):
            a, b = (b, a + b)
        return a

    def binary_to_decimal(binary_str):
        return int(binary_str, 2)
    fib_175th = get_fibonacci_175th()
    decimal_num = binary_to_decimal(binary_str)
    return decimal_num % fib_175th == 0