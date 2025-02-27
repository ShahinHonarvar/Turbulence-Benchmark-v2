def if_decimal_is_divisible(bin_str):
    fib = [0, 1]
    while fib[-1] < 59:
        fib.append(fib[-1] + fib[-2])
    decimal = int(bin_str, 2)
    return decimal % fib[-2] == 0