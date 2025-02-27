def if_decimal_is_divisible(binary_str):

    def fib(x, a=0, b=1):
        if x == 0:
            return a
        return fib(x - 1, b, a + b)
    dec_num = int(binary_str, 2)
    fib_28 = fib(28)
    return dec_num % fib_28 == 0