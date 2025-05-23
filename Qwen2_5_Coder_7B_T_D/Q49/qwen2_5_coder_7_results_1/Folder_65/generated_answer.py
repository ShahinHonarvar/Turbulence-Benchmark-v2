def if_decimal_is_divisible(binary_str):
    fib = [0, 1]
    while len(fib) <= 127:
        fib.append(fib[-1] + fib[-2])
    fib_127 = fib[127]
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_127 == 0