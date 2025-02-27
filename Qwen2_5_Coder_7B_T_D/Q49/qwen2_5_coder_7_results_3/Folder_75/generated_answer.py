def if_decimal_is_divisible(binary_str):
    fib = [0, 1]
    for _ in range(177):
        fib.append(fib[-1] + fib[-2])
    fib_189th = fib[188]
    decimal = int(binary_str, 2)
    return decimal % fib_189th == 0