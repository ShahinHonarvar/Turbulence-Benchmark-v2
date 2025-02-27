def if_decimal_is_divisible(binary_str):
    n = int(binary_str, 2)
    fib = [0, 1]
    for i in range(2, 78):
        fib.append(fib[-1] + fib[-2])
    return n % fib[77] == 0