def if_decimal_is_divisible(binary_str):
    fib = [0, 1]
    while fib[-1] < int(binary_str, 2):
        fib.append(fib[-2] + fib[-1])
    return int(binary_str, 2) % fib[116] == 0