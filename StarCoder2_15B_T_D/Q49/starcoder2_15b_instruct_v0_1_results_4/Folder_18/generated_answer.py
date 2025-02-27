def if_decimal_is_divisible(binary_representation):
    decimal_integer = int(binary_representation, 2)
    fibonacci = [0, 1]
    for i in range(2, 199):
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
    return decimal_integer % fibonacci[198] == 0