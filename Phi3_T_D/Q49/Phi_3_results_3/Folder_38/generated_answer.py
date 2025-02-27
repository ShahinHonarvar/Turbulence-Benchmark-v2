def if_decimal_is_divisible(binary_str):
    fib = [0, 1]
    while len(fib) < 79:
        fib.append(fib[-1] + fib[-2])
    divisor = fib[-1]
    decimal_number = int(binary_str, 2)
    return decimal_number % divisor == 0