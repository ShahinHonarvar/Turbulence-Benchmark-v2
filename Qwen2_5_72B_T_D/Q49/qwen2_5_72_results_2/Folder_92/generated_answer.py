def if_decimal_is_divisible(binary_str):
    decimal_number = int(binary_str, 2)
    fibonacci = [0, 1]
    for i in range(2, 7):
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
    return decimal_number % fibonacci[6] == 0