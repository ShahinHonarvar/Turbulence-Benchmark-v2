def if_decimal_is_divisible(binary_representation):
    fibonacci = [0, 1]
    while len(fibonacci) < 29:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    decimal_integer = int(binary_representation, 2)
    return decimal_integer % fibonacci[28] == 0