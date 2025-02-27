def if_decimal_is_divisible(binary_str):
    fib = [0, 1]
    while len(fib) <= 48:
        fib.append(fib[-1] + fib[-2])

    def binary_to_decimal(binary):
        return int(binary, 2)
    decimal_val = binary_to_decimal(binary_str)
    return decimal_val % fib[48] == 0