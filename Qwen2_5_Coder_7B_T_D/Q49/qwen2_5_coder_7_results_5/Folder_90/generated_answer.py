def if_decimal_is_divisible(binary_str):
    fib_num = 176
    a, b = (0, 1)
    for _ in range(fib_num):
        a, b = (b, a + b)
    decimal_num = int(binary_str, 2)
    return decimal_num % a == 0