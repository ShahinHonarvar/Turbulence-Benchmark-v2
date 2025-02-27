def if_decimal_is_divisible(binary_str):
    fib = [0, 1]
    while len(fib) < 87:
        fib.append(fib[-1] + fib[-2])
    fib_87th = fib[86]
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_87th == 0