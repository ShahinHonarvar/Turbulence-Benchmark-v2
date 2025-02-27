def if_decimal_is_divisible(bin_str):
    fib_cache = {0: 0, 1: 1}

    def fibonacci(n):
        if n not in fib_cache:
            fib_cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return fib_cache[n]
    fib_119 = fibonacci(119)
    decimal_num = int(bin_str, 2)
    if decimal_num % fib_119 == 0:
        return True
    else:
        return False