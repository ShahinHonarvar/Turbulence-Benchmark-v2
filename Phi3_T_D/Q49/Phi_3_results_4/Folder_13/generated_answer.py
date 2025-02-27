def if_decimal_is_divisible(binary_str):
    fib_1 = 0
    fib_2 = 1
    fib_idx = 2
    fib_num = fib_1 + fib_2
    while fib_idx < 174:
        fib_1 = fib_2
        fib_2 = fib_num
        fib_idx += 1
        fib_num = fib_1 + fib_2
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_num == 0