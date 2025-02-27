def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    fibonacci = [0, 1]
    while fibonacci[-1] <= decimal:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return decimal in fibonacci and fibonacci.index(decimal) == 176