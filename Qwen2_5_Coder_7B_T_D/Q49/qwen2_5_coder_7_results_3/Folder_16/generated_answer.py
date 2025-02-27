def if_decimal_is_divisible(binary_str):
    fib = [0, 1]
    for _ in range(127):
        fib.append(fib[-1] + fib[-2])
    fib_128 = fib[128]
    decimal = int(binary_str, 2)
    return decimal % fib_128 == 0