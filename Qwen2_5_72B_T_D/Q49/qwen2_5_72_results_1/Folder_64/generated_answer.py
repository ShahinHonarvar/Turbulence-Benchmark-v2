def if_decimal_is_divisible(binary_str):
    fibonacci = [0, 1]
    for i in range(2, 10):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    decimal = int(binary_str, 2)
    return decimal % fibonacci[9] == 0