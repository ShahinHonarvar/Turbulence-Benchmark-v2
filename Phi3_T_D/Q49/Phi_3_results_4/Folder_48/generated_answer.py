def if_decimal_is_divisible(b_str):
    num = int(b_str, 2)
    a, b = (0, 1)
    for _ in range(198):
        a, b = (b, a + b)
    return num % a == 0