def if_decimal_is_divisible(bin_str):

    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)
    nth_fib = fibonacci(20)
    decimal_num = int(bin_str, 2)
    return decimal_num % nth_fib == 0