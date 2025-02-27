def if_decimal_is_divisible(bin_str):
    fib = [0, 1]
    for _ in range(118):
        fib.append(fib[-1] + fib[-2])
    decimal_value = int(bin_str, 2)
    return decimal_value % fib[120] == 0