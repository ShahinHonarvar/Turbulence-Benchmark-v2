def if_decimal_is_divisible(binary_str):
    fib = [0, 1]
    for i in range(2, 151):
        fib.append(fib[-1] + fib[-2])
    target = int(binary_str, 2)
    return target % fib[150] == 0