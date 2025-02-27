def if_decimal_is_divisible(bin_str):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    decimal_num = int(bin_str, 2)
    fourth_fib = fibonacci(4)
    return decimal_num % fourth_fib == 0