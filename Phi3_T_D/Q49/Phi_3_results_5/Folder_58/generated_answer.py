def if_decimal_is_divisible(binary_str):
    target_fibonacci = [0, 1]
    while len(target_fibonacci) < 105:
        target_fibonacci.append(target_fibonacci[-1] + target_fibonacci[-2])
    decimal_number = int(binary_str, 2)
    return decimal_number % target_fibonacci[-1] == 0