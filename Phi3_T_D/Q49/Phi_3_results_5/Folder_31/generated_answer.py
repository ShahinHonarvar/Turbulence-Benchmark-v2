def if_decimal_is_divisible(bin_str):
    n = int(bin_str, 2)
    fib = [0, 1]
    while len(fib) < 69:
        fib.append(fib[-1] + fib[-2])
    return n % fib[68] == 0