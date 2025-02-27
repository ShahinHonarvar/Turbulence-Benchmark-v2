def if_decimal_is_divisible(binary_rep):
    decimal = int(binary_rep, 2)
    fibonacci = [0, 1]
    for i in range(2, 178):
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
    return decimal % fibonacci[177] == 0