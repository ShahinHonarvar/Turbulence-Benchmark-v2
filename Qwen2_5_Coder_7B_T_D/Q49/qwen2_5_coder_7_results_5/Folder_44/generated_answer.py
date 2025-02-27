def if_decimal_is_divisible(binary_str):
    fib = [0, 1]
    for i in range(2, 159):
        fib.append(fib[-1] + fib[-2])
    fib_159 = fib[159]
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_159 == 0