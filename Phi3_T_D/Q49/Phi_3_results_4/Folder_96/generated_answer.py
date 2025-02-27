def if_decimal_is_divisible(binary_str):
    fibo_numbers = [0, 1]
    while len(fibo_numbers) < 47:
        next_fibo = fibo_numbers[-1] + fibo_numbers[-2]
        fibo_numbers.append(next_fibo)
    decimal_value = int(binary_str, 2)
    return decimal_value % fibo_numbers[46] == 0