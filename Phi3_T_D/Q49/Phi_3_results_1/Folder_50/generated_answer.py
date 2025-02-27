def if_decimal_is_divisible(binary_str):
    fibo_119 = [0, 1]
    while len(fibo_119) < 120:
        fibo_119.append(fibo_119[-1] + fibo_119[-2])
    decimal_value = int(binary_str, 2)
    return decimal_value % fibo_119[-1] == 0