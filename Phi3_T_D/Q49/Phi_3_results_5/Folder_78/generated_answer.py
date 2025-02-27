def if_decimal_is_divisible(binary_str):
    fib = [0, 1]
    while len(fib) < 116:
        fib.append(fib[-1] + fib[-2])
    decimal_int = int(binary_str, 2)
    return decimal_int % fib[-1] == 0