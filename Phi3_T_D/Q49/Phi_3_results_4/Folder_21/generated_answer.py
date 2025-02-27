def if_decimal_is_divisible(binary_str):

    def fib_sequence(n):
        a, b = (0, 1)
        for _ in range(n):
            yield a
            a, b = (b, a + b)
    fib_195 = next((x for i, x in enumerate(fib_sequence(10000)) if i == 195))
    decimal_val = int(binary_str, 2)
    return decimal_val % fib_195 == 0