def if_decimal_is_divisible(b_str):

    def fib(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a

    def binary_to_decimal(b_str):
        return int(b_str, 2)
    fib_num = fib(68)
    decimal_num = binary_to_decimal(b_str)
    return decimal_num % fib_num == 0