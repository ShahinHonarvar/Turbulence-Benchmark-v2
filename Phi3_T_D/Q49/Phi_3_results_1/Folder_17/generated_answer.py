def if_decimal_is_divisible(binary_str):

    def fib(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)
    decimal_value = int(binary_str, 2)
    fib_number_154 = fib(154)
    return decimal_value % fib_number_154 == 0