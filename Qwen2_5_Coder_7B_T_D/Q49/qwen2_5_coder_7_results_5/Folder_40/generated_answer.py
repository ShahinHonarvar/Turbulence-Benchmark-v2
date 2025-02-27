def if_decimal_is_divisible(binary_str):
    fib = [0, 1]
    n = 2
    while True:
        fib.append(fib[n - 1] + fib[n - 2])
        if n >= 3:
            if fib[n] % 4 == 0:
                break
        n += 1
    decimal = int(binary_str, 2)
    return decimal % fib[n] == 0