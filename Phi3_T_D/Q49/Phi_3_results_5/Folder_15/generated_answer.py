def if_decimal_is_divisible(binary_str):
    decimal_num = int(binary_str, 2)
    fibonacci = [0, 1]
    while len(fibonacci) < 10:
        fibonacci.append(fibonacci[-2] + fibonacci[-1])
    return decimal_num % fibonacci[9] == 0