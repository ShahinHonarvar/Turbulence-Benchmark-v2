def if_decimal_is_divisible(binary_str):
    fib = [0, 1]
    while len(fib) < 6:
        fib.append(fib[-1] + fib[-2])
    sixth_fib = fib[5]
    decimal = int(binary_str, 2)
    return decimal % sixth_fib == 0