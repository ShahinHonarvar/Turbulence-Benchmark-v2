def if_decimal_is_divisible(binary_str):
    fib = [0, 1]
    for _ in range(2, 29):
        fib.append(fib[-1] + fib[-2])
    divisor = fib[-1]
    decimal = int(binary_str, 2)
    return decimal % divisor == 0