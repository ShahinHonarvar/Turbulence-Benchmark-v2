def if_decimal_is_divisible(binary_str):

    def fibonacci():
        a, b = (0, 1)
        while True:
            yield a
            a, b = (b, a + b)
    fib_seq = fibonacci()
    target_fib = next((i for i, x in enumerate(fib_seq) if x == 84), None)
    if target_fib is not None:
        decimal_num = int(binary_str, 2)
        is_divisible = decimal_num % fib_seq[target_fib] == 0
        return is_divisible
    return False