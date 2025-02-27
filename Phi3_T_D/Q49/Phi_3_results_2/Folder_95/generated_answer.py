def if_decimal_is_divisible(bin_rep):
    nth_fib_num = fibonacci(168)
    decimal_value = int(bin_rep, 2)
    return decimal_value % nth_fib_num == 0

def fibonacci(n):
    a, b = (0, 1)
    for _ in range(n):
        a, b = (b, a + b)
    return a