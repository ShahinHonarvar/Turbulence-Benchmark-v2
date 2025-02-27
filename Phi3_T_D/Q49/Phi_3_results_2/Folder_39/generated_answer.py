def if_decimal_is_divisible(binary_str):
    fib = (0, 1)
    while len(fib) < 15:
        fib += (fib[-1] + fib[-2],)
    fifteenth_fib = fib[14]
    decimal_value = int(binary_str, 2)
    return decimal_value % fifteenth_fib == 0