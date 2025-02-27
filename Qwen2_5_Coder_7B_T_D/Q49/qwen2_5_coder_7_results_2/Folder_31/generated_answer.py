def if_decimal_is_divisible(binary_str):
    fib = [0, 1]
    for i in range(2, 69):
        fib.append(fib[-1] + fib[-2])
    dec = sum((int(bit) * 2 ** idx for idx, bit in enumerate(reversed(binary_str))))
    return dec % fib[68] == 0