def if_decimal_is_divisible(binary_str):

    def fibo(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    decimal_value = int(binary_str, 2)
    fib_49th = fibo(49)
    return decimal_value % fib_49th == 0