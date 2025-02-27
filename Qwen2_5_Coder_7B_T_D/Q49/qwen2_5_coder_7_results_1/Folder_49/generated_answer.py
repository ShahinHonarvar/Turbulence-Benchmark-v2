def if_decimal_is_divisible(binary_str):
    fibs = [0, 1]
    for i in range(2, 95):
        fibs.append(fibs[-1] + fibs[-2])
    fib_95 = fibs[94]
    decimal = int(binary_str, 2)
    return decimal % fib_95 == 0