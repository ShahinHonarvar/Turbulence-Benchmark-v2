def if_decimal_is_divisible(binary_str):

    def fib_n(n):
        a, b = (0, 1)
        for _ in range(n - 1):
            a, b = (b, a + b)
        return a

    def binary_to_decimal(binary_str):
        return int(binary_str, 2)
    fibo_177 = fib_n(177)
    decimal_value = binary_to_decimal(binary_str)
    return decimal_value % fibo_177 == 0