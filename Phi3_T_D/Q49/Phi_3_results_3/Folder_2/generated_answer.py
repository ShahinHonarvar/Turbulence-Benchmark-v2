def if_decimal_is_divisible(bin_str):
    fib_n = 125
    a, b = (0, 1)
    for _ in range(fib_n):
        a, b = (b, a + b)
    decimal_value = int(bin_str, 2)
    return decimal_value % a == 0