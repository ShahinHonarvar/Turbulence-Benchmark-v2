def if_decimal_is_divisible(binary_repr):
    decimal_int = int(binary_repr, 2)

    def fib(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)
    if decimal_int % fib(56) == 0:
        return True
    else:
        return False