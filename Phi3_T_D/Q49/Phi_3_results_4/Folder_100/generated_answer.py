def if_decimal_is_divisible(binary_str):
    val = int(binary_str, 2)

    def fib(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)
    fib_190 = fib(190)
    return val % fib_190 == 0