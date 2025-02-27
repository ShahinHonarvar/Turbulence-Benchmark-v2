def if_decimal_is_divisible(binary_str):
    fib = [0, 1]
    while fib[-1] < 10 ** len(binary_str):
        fib.append(fib[-1] + fib[-2])
    decimal = int(binary_str, 2)
    return decimal % fib[87] == 0