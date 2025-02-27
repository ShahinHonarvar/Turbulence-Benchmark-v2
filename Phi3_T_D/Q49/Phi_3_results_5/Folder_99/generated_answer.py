def if_decimal_is_divisible(binary_str):

    def fibo(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    decimal_num = int(binary_str, 2)
    fibo_109th = fibo(109)
    return decimal_num % fibo_109th == 0