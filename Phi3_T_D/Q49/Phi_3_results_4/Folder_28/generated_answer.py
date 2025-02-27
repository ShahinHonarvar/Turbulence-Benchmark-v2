def if_decimal_is_divisible(binary_str):
    fibonacci = [0, 1]
    while len(fibonacci) < 105:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    decimal_number = int(binary_str, 2)
    return decimal_number % fibonacci[104] == 0