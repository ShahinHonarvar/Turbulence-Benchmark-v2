def if_decimal_is_divisible(binary_str):
    fibs = [0, 1]
    for _ in range(2, 28):
        fibs.append(fibs[-1] + fibs[-2])
    fib_28 = fibs[27]
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_28 == 0