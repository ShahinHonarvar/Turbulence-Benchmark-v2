def if_decimal_is_divisible(binary_str):

    def fib_n(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    decimal_value = int(binary_str, 2)
    if decimal_value == 0:
        return fib_n(134) % decimal_value == 0
    index = 1
    while True:
        next_fib = fib_n(index)
        if decimal_value % next_fib == 0:
            return True
        if next_fib >= decimal_value:
            break
        index += 1
    return False