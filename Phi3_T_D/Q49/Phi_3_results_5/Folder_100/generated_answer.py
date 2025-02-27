def if_decimal_is_divisible(binary_str):
    fib = [0, 1]
    while len(fib) <= 190:
        fib.append(fib[-1] + fib[-2])
    decimal_val = int(binary_str, 2)
    return decimal_val % fib[190] == 0