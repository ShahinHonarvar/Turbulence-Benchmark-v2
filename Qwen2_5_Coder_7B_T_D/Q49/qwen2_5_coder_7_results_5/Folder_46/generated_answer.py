def if_decimal_is_divisible(binary_str):
    fib = [0, 1]
    for i in range(2, 139):
        fib.append(fib[-1] + fib[-2])
    div = fib[138]
    dec = int(binary_str, 2)
    return dec % div == 0