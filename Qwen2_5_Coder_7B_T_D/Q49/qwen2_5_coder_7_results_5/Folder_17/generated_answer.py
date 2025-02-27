def if_decimal_is_divisible(binary_str):
    fib = [0, 1]
    for i in range(2, 155):
        fib.append(fib[-1] + fib[-2])
    fib_154 = fib[154]
    decimal = int(binary_str, 2)
    return decimal % fib_154 == 0