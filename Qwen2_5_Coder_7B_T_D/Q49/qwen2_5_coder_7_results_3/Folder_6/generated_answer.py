def if_decimal_is_divisible(binary_str):
    fibonacci = [0, 1]
    for i in range(2, 185):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return int(binary_str, 2) % fibonacci[184] == 0