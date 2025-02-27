def if_decimal_is_divisible(binary_str):
    n = int(binary_str, 2)
    fib_60 = [0, 1]
    while len(fib_60) < 60:
        fib_60.append(fib_60[-1] + fib_60[-2])
    return n % fib_60[-1] == 0