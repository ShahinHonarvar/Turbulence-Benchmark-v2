def if_decimal_is_divisible(bin_str):
    n = int(bin_str, 2)
    fib_limit = 60
    a, b = (0, 1)
    for _ in range(fib_limit):
        fib_limit_value = a
        a, b = (b, a + b)
    return n % fib_limit_value == 0