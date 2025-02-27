def if_decimal_is_divisible(binary_str):
    fib = [0, 1]
    while len(fib) < 57:
        fib.append(fib[-1] + fib[-2])
    decimal = int(binary_str, 2)
    return decimal % fib[56] == 0