def if_decimal_is_divisible(binary_str):
    fib_46 = [0, 1, 1]
    while len(fib_46) < 46:
        fib_46.append(fib_46[-1] + fib_46[-2])
    decimal_val = int(binary_str, 2)
    return decimal_val % fib_46[-1] == 0