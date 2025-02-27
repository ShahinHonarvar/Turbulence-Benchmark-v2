def if_decimal_is_divisible(binary_str):
    fib = [0, 1]
    while len(fib) <= 74:
        fib.append(fib[-1] + fib[-2])
    number = int(binary_str, 2)
    return number % fib[74] == 0