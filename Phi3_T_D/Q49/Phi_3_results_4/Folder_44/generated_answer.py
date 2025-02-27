def if_decimal_is_divisible(binary_str):

    def fib(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)
    fib_159 = [fib(i) for i in range(159 + 2)][-1]
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_159 == 0