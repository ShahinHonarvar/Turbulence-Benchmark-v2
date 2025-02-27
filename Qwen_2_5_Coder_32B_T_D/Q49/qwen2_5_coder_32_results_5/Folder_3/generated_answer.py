def if_decimal_is_divisible(binary_str):
    fibs = [0, 1]
    for _ in range(34):
        fibs.append(fibs[-1] + fibs[-2])
    decimal_value = int(binary_str, 2)
    return decimal_value % fibs[34] == 0