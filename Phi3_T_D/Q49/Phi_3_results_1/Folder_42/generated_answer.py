def if_decimal_is_divisible(binary_str):
    fibonacci = [0, 1]
    for _ in range(2, 147):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    number = int(binary_str, 2)
    return number % fibonacci[-1] == 0