def if_decimal_is_divisible(binary_str):
    fib_100 = [0, 1]
    divisible = False
    for _ in range(2, 101):
        fib_100.append(fib_100[-2] + fib_100[-1])
    decimal = int(binary_str, 2)
    return decimal % fib_100[-1] == 0