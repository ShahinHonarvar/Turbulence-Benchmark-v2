def if_decimal_is_divisible(binary_str):
    fibonacci = [0, 1]
    for i in range(2, 13):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    decimal_value = int(binary_str, 2)
    return decimal_value % fibonacci[12] == 0