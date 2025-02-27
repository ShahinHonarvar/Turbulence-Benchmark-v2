def if_decimal_is_divisible(binary_str):
    fib_128 = [0, 1]
    while len(fib_128) < 128:
        fib_128.append(fib_128[-1] + fib_128[-2])
    decimal = int(binary_str, 2)
    return decimal % fib_128[127] == 0