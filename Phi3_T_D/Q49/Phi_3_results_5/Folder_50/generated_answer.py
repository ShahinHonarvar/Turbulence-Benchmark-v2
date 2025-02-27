def if_decimal_is_divisible(binary_str):
    dec = int(binary_str, 2)
    fib_119 = [0, 1]
    while len(fib_119) < 120:
        fib_119.append(fib_119[-1] + fib_119[-2])
    return dec % fib_119[-1] == 0