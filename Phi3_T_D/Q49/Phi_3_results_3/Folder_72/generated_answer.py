def if_decimal_is_divisible(binary_str):
    fib_175 = [0, 1]
    i = 2
    while len(fib_175) < 175:
        fib_175.append(fib_175[i - 1] + fib_175[i - 2])
        i += 1
    decimal_val = int(binary_str, 2)
    return decimal_val % fib_175[-1] == 0