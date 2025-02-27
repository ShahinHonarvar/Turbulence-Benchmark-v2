def if_decimal_is_divisible(bin_str):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    fib_number = fibonacci(33)
    decimal_number = int(bin_str, 2)
    return decimal_number % fib_number == 0