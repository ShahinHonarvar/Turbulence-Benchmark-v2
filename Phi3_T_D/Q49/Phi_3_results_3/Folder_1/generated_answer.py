def if_decimal_is_divisible(binary_str):
    fib_hundred = [0, 1]
    while len(fib_hundred) < 90:
        fib_hundred.append(fib_hundred[-1] + fib_hundred[-2])
    decimal = int(binary_str, 2)
    return decimal % fib_hundred[-1] == 0