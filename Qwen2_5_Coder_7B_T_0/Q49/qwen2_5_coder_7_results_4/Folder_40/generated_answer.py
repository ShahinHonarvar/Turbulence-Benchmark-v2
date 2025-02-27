def if_decimal_is_divisible(binary_str):
    fib = [0, 1]
    for i in range(2, 10):
        fib.append(fib[-1] + fib[-2])
    fourth_fib = fib[3]
    decimal = int(binary_str, 2)
    return decimal % fourth_fib == 0