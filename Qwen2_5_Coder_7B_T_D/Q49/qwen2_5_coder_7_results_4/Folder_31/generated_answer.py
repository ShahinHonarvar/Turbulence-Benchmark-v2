import functools

def if_decimal_is_divisible(binary_str):

    def fib(n, a=0, b=1):
        return a if n == 0 else fib(n - 1, b, a + b)
    fibonacci_69 = functools.reduce(lambda a, b: a + b, [fib(i) for i in range(70)])
    decimal_num = int(binary_str, 2)
    return decimal_num % fibonacci_69 == 0