def if_decimal_is_divisible(bin_str):

    def fibonacci(n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        return fibonacci(n - 1) + fibonacci(n - 2)
    decimal = int(bin_str, 2)
    fib_120 = fibonacci(120)
    return decimal % fib_120 == 0