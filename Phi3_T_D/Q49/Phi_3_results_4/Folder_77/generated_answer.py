def if_decimal_is_divisible(binary_str):
    fib = [0, 1]
    while len(fib) <= 110:
        fib.append(fib[-1] + fib[-2])
    fib_110th = fib[109]
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_110th == 0