def if_decimal_is_divisible(bin_string):
    decimal = int(bin_string, 2)
    fibonacci = [0, 1]
    while len(fibonacci) < 55:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return decimal % fibonacci[-1] == 0