def if_decimal_is_divisible(binary_str):
    fib = [0, 1]
    while len(fib) < 14:
        fib.append(fib[-1] + fib[-2])
    fib_13th = fib[-1]
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_13th == 0