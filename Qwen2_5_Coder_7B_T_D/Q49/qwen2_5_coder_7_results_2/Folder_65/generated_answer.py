def if_decimal_is_divisible(binary_str):
    fib_127 = 1
    fib_126 = 1
    for _ in range(124):
        fib_127, fib_126 = (fib_126, fib_127 + fib_126)
    decimal = int(binary_str, 2)
    return decimal % fib_127 == 0